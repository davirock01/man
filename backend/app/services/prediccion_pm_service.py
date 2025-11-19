from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from datetime import datetime, timedelta
from typing import Optional

from app.models.salud_vehiculo import PrediccionPM
from app.models.vehiculo import Vehiculo, ConfigPM
from app.models.orden_trabajo import OrdenTrabajo
from app.services.alert_service import AlertService
from app.core.config import settings


class PrediccionPMService:
    """Service for PM (Preventive Maintenance) predictions."""
    
    def __init__(self, db: AsyncSession):
        self.db = db
        self.alert_service = AlertService(db)
    
    async def calculate_next_pm(self, vehiculo_id: int) -> PrediccionPM:
        """
        Calculate next PM date and km for a vehicle.
        """
        # Get vehicle
        result = await self.db.execute(
            select(Vehiculo).where(Vehiculo.id == vehiculo_id)
        )
        vehiculo = result.scalar_one_or_none()
        
        if not vehiculo:
            raise ValueError(f"Vehicle {vehiculo_id} not found")
        
        # Get PM config for vehicle type
        result = await self.db.execute(
            select(ConfigPM).where(ConfigPM.vehiculo_tipo == vehiculo.vehiculo_tipo)
        )
        config = result.scalar_one_or_none()
        
        if not config:
            # Use default values
            politica_km = 5000.0
            politica_tiempo = 90
            umbral_km = settings.PM_ALERT_THRESHOLD_KM
            umbral_tiempo = settings.PM_ALERT_THRESHOLD_TIME
        else:
            politica_km = config.politica_km
            politica_tiempo = config.politica_tiempo
            umbral_km = config.umbral_km_alerta
            umbral_tiempo = config.umbral_tiempo_alerta
        
        # Get last PM
        result = await self.db.execute(
            select(OrdenTrabajo)
            .where(
                OrdenTrabajo.vehiculo_id == vehiculo_id,
                OrdenTrabajo.tipo == "PM_PREVENTIVO",
                OrdenTrabajo.estado == "COMPLETADA"
            )
            .order_by(OrdenTrabajo.fecha_fin.desc())
        )
        ultimo_pm = result.scalar_one_or_none()
        
        if ultimo_pm:
            km_ultimo_pm = vehiculo.odometro_actual - politica_km  # Approximate
            fecha_ultimo_pm = ultimo_pm.fecha_fin
        else:
            km_ultimo_pm = 0.0
            fecha_ultimo_pm = None
        
        # Calculate next PM
        km_proximo_pm = km_ultimo_pm + politica_km
        fecha_proximo_pm = (fecha_ultimo_pm or datetime.utcnow()) + timedelta(days=politica_tiempo)
        
        # Get or create prediction
        result = await self.db.execute(
            select(PrediccionPM).where(PrediccionPM.vehiculo_id == vehiculo_id)
        )
        prediccion = result.scalar_one_or_none()
        
        if prediccion:
            # Update existing
            prediccion.km_actual = vehiculo.odometro_actual
            prediccion.fecha_actual = datetime.utcnow()
            prediccion.km_ultimo_pm = km_ultimo_pm
            prediccion.fecha_ultimo_pm = fecha_ultimo_pm
            prediccion.km_proximo_pm = km_proximo_pm
            prediccion.fecha_proximo_pm = fecha_proximo_pm
            prediccion.umbral_km_configurado = politica_km
            prediccion.umbral_tiempo_configurado = politica_tiempo
        else:
            # Create new
            prediccion = PrediccionPM(
                vehiculo_id=vehiculo_id,
                km_actual=vehiculo.odometro_actual,
                fecha_actual=datetime.utcnow(),
                km_ultimo_pm=km_ultimo_pm,
                fecha_ultimo_pm=fecha_ultimo_pm,
                km_proximo_pm=km_proximo_pm,
                fecha_proximo_pm=fecha_proximo_pm,
                umbral_km_configurado=politica_km,
                umbral_tiempo_configurado=politica_tiempo,
                alerta_generada="NO",
            )
            self.db.add(prediccion)
        
        await self.db.commit()
        await self.db.refresh(prediccion)
        
        return prediccion
    
    async def check_pm_threshold(self, vehiculo_id: int):
        """
        Check if vehicle is approaching PM threshold and generate alert if needed.
        """
        # Calculate or update prediction
        prediccion = await self.calculate_next_pm(vehiculo_id)
        
        # Check km threshold
        km_restantes = prediccion.km_proximo_pm - prediccion.km_actual
        km_porcentaje = prediccion.km_actual / prediccion.km_proximo_pm if prediccion.km_proximo_pm > 0 else 0
        
        # Check time threshold
        dias_restantes = (prediccion.fecha_proximo_pm - datetime.utcnow()).days if prediccion.fecha_proximo_pm else 999
        
        # Determine alert level
        alerta_generada = "NO"
        criticidad = "BAJA"
        
        if km_porcentaje >= 1.0 or dias_restantes <= 0:
            alerta_generada = "URGENTE"
            criticidad = "ALTA"
            mensaje = f"PM VENCIDO: Vehículo ha excedido el intervalo de mantenimiento"
        elif km_porcentaje >= 0.9 or dias_restantes <= 7:
            alerta_generada = "ADVERTENCIA"
            criticidad = "MEDIA"
            mensaje = f"PM PRÓXIMO: {km_restantes:.0f} km o {dias_restantes} días restantes"
        
        # Generate alert if needed and not already generated
        if alerta_generada != "NO" and prediccion.alerta_generada != alerta_generada:
            await self.alert_service.generate_predictive_alert(
                vehiculo_id=vehiculo_id,
                tipo="PM_PROXIMA" if alerta_generada == "ADVERTENCIA" else "PM_VENCIDA",
                mensaje=mensaje,
                criticidad=criticidad,
                datos_json={
                    "km_actual": prediccion.km_actual,
                    "km_proximo_pm": prediccion.km_proximo_pm,
                    "km_restantes": km_restantes,
                    "dias_restantes": dias_restantes,
                },
                prediccion_pm_id=prediccion.id,
            )
            
            # Update prediction alert status
            prediccion.alerta_generada = alerta_generada
            await self.db.commit()


