from sqlalchemy.orm import Session
from sqlalchemy import func
from uuid import UUID
from datetime import datetime, timedelta
from typing import Dict, Any

from app.models.salud_vehiculo import SaludVehiculo
from app.models.dvir import DVIR
from app.models.alert import AlertaReactiva
from app.models.patron_recurrente import PatronRecurrente
from app.models.work_order import OrdenWork


class HealthScoreService:
    @staticmethod
    def calculate_health_score(db: Session, vehiculo_id: UUID) -> float:
        """
        Calculate vehicle health score (0-100).
        
        Formula:
        score = 100
        - dvirs_criticos_30d * 5 puntos
        - alertas_reactivas_abiertas * 3 puntos
        - pm_atrasados * 10 puntos
        - patrones_recurrentes * 7 puntos
        + (dias_sin_incidente / 30) * 5 puntos
        """
        score = 100.0
        detalle = {}
        
        fecha_30d = datetime.utcnow() - timedelta(days=30)
        
        # DVIRs críticos en los últimos 30 días
        dvirs_criticos = db.query(func.count(DVIR.id)).filter(
            DVIR.vehiculo_id == vehiculo_id,
            DVIR.estado_resumen == "CRITICO",
            DVIR.timestamp >= fecha_30d
        ).scalar() or 0
        
        score -= dvirs_criticos * 5
        detalle['dvir_criticos_30d'] = dvirs_criticos
        
        # Alertas reactivas abiertas
        alertas_abiertas = db.query(func.count(AlertaReactiva.id)).filter(
            AlertaReactiva.vehiculo_id == vehiculo_id,
            AlertaReactiva.estado == "PENDIENTE"
        ).scalar() or 0
        
        score -= alertas_abiertas * 3
        detalle['alertas_reactivas_abiertas'] = alertas_abiertas
        
        # PM atrasados (simplificado: OTs PM_PREVENTIVO pendientes)
        pm_atrasados = db.query(func.count(OrdenWork.id)).filter(
            OrdenWork.vehiculo_id == vehiculo_id,
            OrdenWork.tipo == "PM_PREVENTIVO",
            OrdenWork.estado.in_(["PENDIENTE", "ASIGNADA"]),
            OrdenWork.fecha_programada < datetime.utcnow().date()
        ).scalar() or 0
        
        score -= pm_atrasados * 10
        detalle['pm_atrasados'] = pm_atrasados
        
        # Patrones recurrentes activos
        patrones = db.query(func.count(PatronRecurrente.id)).filter(
            PatronRecurrente.vehiculo_id == vehiculo_id,
            PatronRecurrente.estado == "ACTIVO"
        ).scalar() or 0
        
        score -= patrones * 7
        detalle['patrones_recurrentes'] = patrones
        
        # Días sin incidente (último DVIR crítico o alerta)
        ultimo_incidente = db.query(func.max(DVIR.timestamp)).filter(
            DVIR.vehiculo_id == vehiculo_id,
            DVIR.estado_resumen == "CRITICO"
        ).scalar()
        
        if ultimo_incidente:
            dias_sin_incidente = (datetime.utcnow() - ultimo_incidente).days
        else:
            dias_sin_incidente = 30  # Default if no incidents
        
        score += (min(dias_sin_incidente, 30) / 30) * 5
        detalle['dias_sin_incidente'] = dias_sin_incidente
        
        # Clamp score between 0 and 100
        final_score = max(0.0, min(100.0, score))
        detalle['score_final'] = final_score
        
        return final_score, detalle
    
    @staticmethod
    def calculate_and_save(db: Session, vehiculo_id: UUID) -> SaludVehiculo:
        """Calculate and save vehicle health score."""
        score, detalle = HealthScoreService.calculate_health_score(db, vehiculo_id)
        
        # Update or create health record
        salud = db.query(SaludVehiculo).filter(
            SaludVehiculo.vehiculo_id == vehiculo_id
        ).first()
        
        if salud:
            salud.score_salud = score
            salud.fecha_calculo = datetime.utcnow()
            salud.detalle_json = detalle
            salud.updated_at = datetime.utcnow()
        else:
            salud = SaludVehiculo(
                vehiculo_id=vehiculo_id,
                score_salud=score,
                fecha_calculo=datetime.utcnow(),
                detalle_json=detalle
            )
            db.add(salud)
        
        db.flush()
        return salud
    
    @staticmethod
    def get_health_detail(db: Session, vehiculo_id: UUID) -> Dict[str, Any]:
        """Get detailed health information for a vehicle."""
        salud = db.query(SaludVehiculo).filter(
            SaludVehiculo.vehiculo_id == vehiculo_id
        ).first()
        
        if not salud:
            # Calculate if not exists
            salud = HealthScoreService.calculate_and_save(db, vehiculo_id)
            db.commit()
        
        return {
            "vehiculo_id": str(vehiculo_id),
            "score": float(salud.score_salud),
            "fecha_calculo": salud.fecha_calculo,
            "detalle": salud.detalle_json or {}
        }

