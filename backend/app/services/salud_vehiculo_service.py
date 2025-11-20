from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, func
from datetime import datetime, timedelta
from typing import Optional

from app.models.salud_vehiculo import SaludVehiculo
from app.models.dvir import DVIR, DVIRItem, EventoConducta
from app.models.orden_trabajo import OrdenTrabajo


class SaludVehiculoService:
    """Service for calculating and managing vehicle health scores."""
    
    def __init__(self, db: AsyncSession):
        self.db = db
    
    async def calculate_health_score(self, vehiculo_id: int) -> SaludVehiculo:
        """
        Calculate vehicle health score based on multiple factors.
        
        Score calculation (0-100):
        - DVIR score (40%): Based on recent DVIR status
        - Events score (30%): Based on driving behavior events
        - OT score (20%): Based on maintenance history
        - PM compliance (10%): Based on preventive maintenance adherence
        """
        # Get or create health record
        result = await self.db.execute(
            select(SaludVehiculo).where(SaludVehiculo.vehiculo_id == vehiculo_id)
        )
        salud = result.scalar_one_or_none()
        
        # Calculate sub-scores
        dvir_score = await self._calculate_dvir_score(vehiculo_id)
        eventos_score = await self._calculate_eventos_score(vehiculo_id)
        ot_score = await self._calculate_ot_score(vehiculo_id)
        pm_compliance_score = await self._calculate_pm_compliance_score(vehiculo_id)
        
        # Weighted average
        score_total = (
            dvir_score * 0.40 +
            eventos_score * 0.30 +
            ot_score * 0.20 +
            pm_compliance_score * 0.10
        )
        
        # Determine classification
        if score_total >= 90:
            clasificacion = "EXCELENTE"
        elif score_total >= 75:
            clasificacion = "BUENO"
        elif score_total >= 60:
            clasificacion = "REGULAR"
        elif score_total >= 40:
            clasificacion = "MALO"
        else:
            clasificacion = "CRITICO"
        
        detalle = {
            "dvir_score": dvir_score,
            "eventos_score": eventos_score,
            "ot_score": ot_score,
            "pm_compliance": pm_compliance_score,
            "fecha_calculo": datetime.utcnow().isoformat(),
        }
        
        if salud:
            # Update existing
            salud.score_salud = score_total
            salud.fecha_calculo = datetime.utcnow()
            salud.detalle_json = detalle
            salud.clasificacion = clasificacion
        else:
            # Create new
            salud = SaludVehiculo(
                vehiculo_id=vehiculo_id,
                score_salud=score_total,
                fecha_calculo=datetime.utcnow(),
                detalle_json=detalle,
                clasificacion=clasificacion,
            )
            self.db.add(salud)
        
        await self.db.commit()
        await self.db.refresh(salud)
        
        return salud
    
    async def _calculate_dvir_score(self, vehiculo_id: int) -> float:
        """Calculate DVIR score based on last 10 DVIRs."""
        # Get last 10 DVIRs
        result = await self.db.execute(
            select(DVIR)
            .where(DVIR.vehiculo_id == vehiculo_id)
            .order_by(DVIR.timestamp.desc())
            .limit(10)
        )
        dvirs = result.scalars().all()
        
        if not dvirs:
            return 100.0  # No DVIRs yet, assume good
        
        # Score based on status
        score_total = 0
        for dvir in dvirs:
            if dvir.estado_resumen == "OK":
                score_total += 100
            elif dvir.estado_resumen == "ALERTA":
                score_total += 70
            else:  # CRITICO
                score_total += 30
        
        return score_total / len(dvirs)
    
    async def _calculate_eventos_score(self, vehiculo_id: int) -> float:
        """Calculate events score based on driving behavior in last 7 days."""
        fecha_limite = datetime.utcnow() - timedelta(days=7)
        
        result = await self.db.execute(
            select(func.count(EventoConducta.id))
            .where(
                EventoConducta.vehiculo_id == vehiculo_id,
                EventoConducta.timestamp >= fecha_limite,
                EventoConducta.severidad == "SEVERO"
            )
        )
        eventos_severos = result.scalar() or 0
        
        # Penalize for severe events
        # 0 events = 100, 1-2 events = 80, 3-5 events = 60, 6-10 events = 40, 10+ = 20
        if eventos_severos == 0:
            return 100.0
        elif eventos_severos <= 2:
            return 80.0
        elif eventos_severos <= 5:
            return 60.0
        elif eventos_severos <= 10:
            return 40.0
        else:
            return 20.0
    
    async def _calculate_ot_score(self, vehiculo_id: int) -> float:
        """Calculate OT score based on maintenance history in last 90 days."""
        fecha_limite = datetime.utcnow() - timedelta(days=90)
        
        # Count OTs by type
        result = await self.db.execute(
            select(OrdenTrabajo)
            .where(
                OrdenTrabajo.vehiculo_id == vehiculo_id,
                OrdenTrabajo.fecha_creacion >= fecha_limite
            )
        )
        ots = result.scalars().all()
        
        if not ots:
            return 100.0  # No OTs needed recently
        
        # Count by type
        preventivo_count = len([ot for ot in ots if ot.tipo == "PM_PREVENTIVO"])
        correctivo_count = len([ot for ot in ots if ot.tipo == "CORRECTIVO"])
        emergencia_count = len([ot for ot in ots if ot.tipo == "EMERGENCIA"])
        
        # Good ratio: mostly preventive, few corrective, no emergencies
        if emergencia_count > 0:
            base_score = 40.0
        elif correctivo_count > preventivo_count:
            base_score = 60.0
        elif correctivo_count > 0:
            base_score = 80.0
        else:
            base_score = 100.0
        
        return base_score
    
    async def _calculate_pm_compliance_score(self, vehiculo_id: int) -> float:
        """Calculate PM compliance score."""
        # This would check if vehicle is up to date with PM schedule
        # For now, return a default score
        # TODO: Implement based on PrediccionPM
        return 85.0
    
    async def update_severidad_uso(self, vehiculo_id: int):
        """Update severity of use based on recent driving events."""
        # This would be called by EventosConductaJob
        # Implementation depends on specific business logic
        pass

