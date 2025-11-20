from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from datetime import datetime, timedelta
from typing import Optional, List

from app.models.alerta import AlertaReactiva, AlertaPredictiva, PatronRecurrente
from app.models.dvir import DVIRItem
from app.core.config import settings


class AlertService:
    """Service for alert generation and management."""
    
    def __init__(self, db: AsyncSession):
        self.db = db
    
    async def generate_reactive_alert(
        self,
        vehiculo_id: int,
        origen: str,
        mensaje: str,
        componente_afectado: str,
        criticidad: str,
        origen_dvir_id: Optional[int] = None,
        origen_evento_id: Optional[int] = None,
    ) -> AlertaReactiva:
        """
        Generate a reactive alert.
        
        Args:
            vehiculo_id: Vehicle ID
            origen: Alert origin (DVIR, DEFECTO_RUTA, CONDUCTOR, SISTEMA)
            mensaje: Alert message
            componente_afectado: Affected component
            criticidad: Criticality (BAJA, MEDIA, ALTA, CRITICA)
            origen_dvir_id: DVIR ID if origin is DVIR
            origen_evento_id: Event ID if origin is an event
        """
        alerta = AlertaReactiva(
            vehiculo_id=vehiculo_id,
            origen=origen,
            origen_dvir_id=origen_dvir_id,
            origen_evento_id=origen_evento_id,
            mensaje=mensaje,
            componente_afectado=componente_afectado,
            criticidad=criticidad,
            estado="ACTIVA",
        )
        
        self.db.add(alerta)
        await self.db.commit()
        await self.db.refresh(alerta)
        
        # Publish event for notifications
        from app.utils.events import event_bus
        await event_bus.publish("alerta_reactiva", {
            "alerta_id": alerta.id,
            "vehiculo_id": vehiculo_id,
            "criticidad": criticidad,
            "mensaje": mensaje,
        })
        
        return alerta
    
    async def generate_predictive_alert(
        self,
        vehiculo_id: int,
        tipo: str,
        mensaje: str,
        criticidad: str,
        datos_json: Optional[dict] = None,
        prediccion_pm_id: Optional[int] = None,
    ) -> AlertaPredictiva:
        """
        Generate a predictive alert.
        
        Args:
            vehiculo_id: Vehicle ID
            tipo: Alert type (PM_PROXIMA, PM_VENCIDA, PATRON_DETECTADO)
            mensaje: Alert message
            criticidad: Criticality (BAJA, MEDIA, ALTA, CRITICA)
            datos_json: Additional data
            prediccion_pm_id: PM prediction ID
        """
        alerta = AlertaPredictiva(
            vehiculo_id=vehiculo_id,
            tipo=tipo,
            mensaje=mensaje,
            criticidad=criticidad,
            estado="ACTIVA",
            datos_json=datos_json,
            prediccion_pm_id=prediccion_pm_id,
        )
        
        self.db.add(alerta)
        await self.db.commit()
        await self.db.refresh(alerta)
        
        # Publish event for notifications
        from app.utils.events import event_bus
        await event_bus.publish("alerta_predictiva", {
            "alerta_id": alerta.id,
            "vehiculo_id": vehiculo_id,
            "tipo": tipo,
            "criticidad": criticidad,
            "mensaje": mensaje,
        })
        
        return alerta
    
    async def check_recurring_patterns(self, vehiculo_id: int) -> List[PatronRecurrente]:
        """
        Check for recurring patterns in DVIRs for a vehicle.
        
        Detects when the same defect appears >= 3 times in the last 30 days.
        """
        fecha_limite = datetime.utcnow() - timedelta(days=settings.PATTERN_DETECTION_DAYS)
        
        # Get DVIR items from last 30 days for this vehicle
        from app.models.dvir import DVIR
        result = await self.db.execute(
            select(DVIRItem)
            .join(DVIR, DVIRItem.dvir_id == DVIR.id)
            .where(
                DVIR.vehiculo_id == vehiculo_id,
                DVIR.timestamp >= fecha_limite,
                DVIRItem.estado_item.in_(["ALERTA", "CRITICO"])
            )
        )
        items = result.scalars().all()
        
        # Count occurrences by component
        defect_counts = {}
        defect_details = {}
        
        for item in items:
            key = f"{item.componente}:{item.estado_item}"
            if key not in defect_counts:
                defect_counts[key] = 0
                defect_details[key] = []
            
            defect_counts[key] += 1
            defect_details[key].append({
                "dvir_id": item.dvir_id,
                "fecha": item.creado_en.isoformat(),
                "comentario": item.comentario,
            })
        
        # Create patterns for defects that appear >= min occurrences
        patrones_creados = []
        
        for key, count in defect_counts.items():
            if count >= settings.PATTERN_MIN_OCCURRENCES:
                componente, tipo_defecto = key.split(":")
                
                # Check if pattern already exists
                result = await self.db.execute(
                    select(PatronRecurrente)
                    .where(
                        PatronRecurrente.vehiculo_id == vehiculo_id,
                        PatronRecurrente.componente == componente,
                        PatronRecurrente.tipo_defecto == tipo_defecto,
                        PatronRecurrente.estado == "ACTIVO"
                    )
                )
                patron_existente = result.scalar_one_or_none()
                
                if not patron_existente:
                    # Create new pattern
                    detalles = defect_details[key]
                    criticidad = "ALTA" if tipo_defecto == "CRITICO" else "MEDIA"
                    
                    patron = PatronRecurrente(
                        vehiculo_id=vehiculo_id,
                        componente=componente,
                        tipo_defecto=tipo_defecto,
                        veces_30d=count,
                        fecha_primera_ocurrencia=min(d["fecha"] for d in detalles),
                        fecha_ultima_ocurrencia=max(d["fecha"] for d in detalles),
                        criticidad=criticidad,
                        estado="ACTIVO",
                        detalles_json={"ocurrencias": detalles},
                    )
                    
                    self.db.add(patron)
                    patrones_creados.append(patron)
                    
                    # Generate alert for pattern
                    await self.generate_reactive_alert(
                        vehiculo_id=vehiculo_id,
                        origen="SISTEMA",
                        mensaje=f"Patrón recurrente detectado: {componente} con {count} ocurrencias en 30 días",
                        componente_afectado=componente,
                        criticidad=criticidad,
                    )
        
        if patrones_creados:
            await self.db.commit()
            for patron in patrones_creados:
                await self.db.refresh(patron)
        
        return patrones_creados


