from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, update
from datetime import datetime
from typing import Optional

from app.models.dvir import DVIR, DVIRItem
from app.models.vehiculo import Vehiculo
from app.models.alerta import AlertaReactiva
from app.schemas.dvir import DVIRCreate
from app.services.alert_service import AlertService
from app.services.salud_vehiculo_service import SaludVehiculoService


class DVIRService:
    """Service for DVIR operations."""
    
    def __init__(self, db: AsyncSession):
        self.db = db
        self.alert_service = AlertService(db)
        self.salud_service = SaludVehiculoService(db)
    
    async def create_dvir(self, dvir_data: DVIRCreate, conductor_id: int) -> DVIR:
        """
        Create a new DVIR and process it.
        
        Steps:
        1. Create DVIR with items
        2. Determine overall status (OK/ALERTA/CRITICO)
        3. If critical items, generate reactive alert and change vehicle status
        4. Update vehicle odometer
        5. Recalculate health score
        6. Check for patterns and PM predictions
        """
        # Determine overall status
        estado_resumen = self._determine_estado_resumen(dvir_data.items)
        
        # Create DVIR
        dvir = DVIR(
            vehiculo_id=dvir_data.vehiculo_id,
            conductor_id=conductor_id,
            odometro=dvir_data.odometro,
            gps_lat=dvir_data.gps_lat,
            gps_lng=dvir_data.gps_lng,
            estado_resumen=estado_resumen,
            firma_url=dvir_data.firma_url,
            firma_nombre=dvir_data.firma_nombre,
            comentarios=dvir_data.comentarios,
            modo_offline_flag=dvir_data.modo_offline_flag,
            sincronizado_en=None if dvir_data.modo_offline_flag else datetime.utcnow(),
        )
        
        self.db.add(dvir)
        await self.db.flush()  # Get DVIR ID
        
        # Create DVIR items
        for item_data in dvir_data.items:
            item = DVIRItem(
                dvir_id=dvir.id,
                componente=item_data.componente,
                categoria=item_data.categoria,
                estado_item=item_data.estado_item,
                comentario=item_data.comentario,
                foto_url=item_data.foto_url,
            )
            self.db.add(item)
        
        await self.db.commit()
        await self.db.refresh(dvir)
        
        # Process DVIR completion (async triggers)
        await self.process_dvir_completion(dvir)
        
        return dvir
    
    def _determine_estado_resumen(self, items) -> str:
        """Determine overall DVIR status based on items."""
        has_critico = any(item.estado_item == "CRITICO" for item in items)
        has_alerta = any(item.estado_item == "ALERTA" for item in items)
        
        if has_critico:
            return "CRITICO"
        elif has_alerta:
            return "ALERTA"
        else:
            return "OK"
    
    async def process_dvir_completion(self, dvir: DVIR):
        """
        Process DVIR after creation.
        
        Triggers:
        1. Check for critical items -> reactive alert + vehicle status change
        2. Update vehicle odometer
        3. Recalculate health score
        4. Check PM predictions
        """
        # Get DVIR items
        result = await self.db.execute(
            select(DVIRItem).where(DVIRItem.dvir_id == dvir.id)
        )
        items = result.scalars().all()
        
        # Check for critical items
        critical_items = [item for item in items if item.estado_item == "CRITICO"]
        
        if critical_items:
            # Generate reactive alert
            componentes = ", ".join([item.componente for item in critical_items])
            await self.alert_service.generate_reactive_alert(
                vehiculo_id=dvir.vehiculo_id,
                origen="DVIR",
                mensaje=f"DVIR con ítems críticos detectados: {componentes}",
                componente_afectado=componentes,
                criticidad="CRITICA",
                origen_dvir_id=dvir.id,
            )
            
            # Change vehicle status to NO_OPERATIVO
            await self.db.execute(
                update(Vehiculo)
                .where(Vehiculo.id == dvir.vehiculo_id)
                .values(estado_operativo="NO_OPERATIVO")
            )
        
        # Update vehicle odometer
        await self.db.execute(
            update(Vehiculo)
            .where(Vehiculo.id == dvir.vehiculo_id)
            .values(
                odometro_actual=dvir.odometro,
                ultima_lat=dvir.gps_lat,
                ultima_lng=dvir.gps_lng,
                ultima_actualizacion_gps=datetime.utcnow() if dvir.gps_lat else None,
            )
        )
        
        # Recalculate health score
        await self.salud_service.calculate_health_score(dvir.vehiculo_id)
        
        # Check PM predictions (will be done by PrediccionPMService)
        from app.services.prediccion_pm_service import PrediccionPMService
        pm_service = PrediccionPMService(self.db)
        await pm_service.check_pm_threshold(dvir.vehiculo_id)
        
        await self.db.commit()
    
    async def check_critical_items(self, dvir_id: int) -> bool:
        """Check if DVIR has critical items."""
        result = await self.db.execute(
            select(DVIRItem)
            .where(
                DVIRItem.dvir_id == dvir_id,
                DVIRItem.estado_item == "CRITICO"
            )
        )
        critical_items = result.scalars().all()
        
        return len(critical_items) > 0


