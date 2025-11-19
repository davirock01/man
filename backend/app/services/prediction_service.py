from sqlalchemy.orm import Session
from sqlalchemy import func, desc
from uuid import UUID
from datetime import datetime, timedelta, date
from typing import Optional

from app.models.prediccion_pm import PrediccionPM
from app.models.vehiculo import Vehiculo
from app.models.config_pm import ConfigPM
from app.models.work_order import OrdenWork
from app.models.severidad_uso import SeveridadUso
from app.models.evento_conducta import EventoConducta
from app.services.alert_service import AlertService


class PredictionService:
    @staticmethod
    def calculate_next_pm(db: Session, vehiculo_id: UUID) -> Optional[PrediccionPM]:
        """
        Calculate next PM for a vehicle based on km and time policies.
        
        Adjusts intervals based on severity of use.
        """
        vehiculo = db.query(Vehiculo).filter(Vehiculo.id == vehiculo_id).first()
        if not vehiculo:
            return None
        
        # Get PM configuration for vehicle type
        config = db.query(ConfigPM).filter(ConfigPM.vehiculo_tipo == vehiculo.tipo).first()
        if not config:
            # Use defaults if no config
            config_km = 10000
            config_dias = 180
            umbral_alerta = 0.90
        else:
            config_km = config.politica_km
            config_dias = config.politica_dias
            umbral_alerta = float(config.umbral_alerta_pct)
        
        # Get last PM (completed PM_PREVENTIVO work order)
        ultima_pm = db.query(OrdenWork).filter(
            OrdenWork.vehiculo_id == vehiculo_id,
            OrdenWork.tipo == "PM_PREVENTIVO",
            OrdenWork.estado == "COMPLETADA"
        ).order_by(desc(OrdenWork.fecha_fin)).first()
        
        if ultima_pm:
            km_desde_ultima_pm = vehiculo.odometro_actual - (ultima_pm.contexto_json or {}).get("odometro_inicio", 0)
            fecha_ultima_pm = ultima_pm.fecha_fin.date() if ultima_pm.fecha_fin else date.today()
        else:
            # No previous PM, assume vehicle is new
            km_desde_ultima_pm = vehiculo.odometro_actual
            fecha_ultima_pm = date.today() - timedelta(days=1)
        
        # Calculate km until next PM
        km_faltantes = config_km - km_desde_ultima_pm
        
        # Adjust based on severity of use
        severidad_reciente = PredictionService.get_severidad_reciente(db, vehiculo_id, dias=30)
        if severidad_reciente == "SEVERO":
            km_faltantes = int(km_faltantes * 0.85)  # Reduce interval by 15%
        
        km_proximo_pm = vehiculo.odometro_actual + km_faltantes
        
        # Estimate days until PM based on average km/day
        avg_km_per_day = PredictionService.estimate_avg_km_per_day(db, vehiculo_id)
        if avg_km_per_day > 0:
            dias_hasta_pm = int(km_faltantes / avg_km_per_day)
        else:
            dias_hasta_pm = 30  # Default
        
        fecha_proximo_pm = date.today() + timedelta(days=dias_hasta_pm)
        
        # Create or update prediction
        prediccion = db.query(PrediccionPM).filter(
            PrediccionPM.vehiculo_id == vehiculo_id
        ).order_by(desc(PrediccionPM.created_at)).first()
        
        if not prediccion or (datetime.utcnow() - prediccion.created_at).days >= 1:
            # Create new prediction (daily)
            prediccion = PrediccionPM(
                vehiculo_id=vehiculo_id,
                km_actual=vehiculo.odometro_actual,
                km_proximo_pm=km_proximo_pm,
                fecha_proximo_pm=fecha_proximo_pm,
                dias_hasta_pm=dias_hasta_pm,
                prob_falla=None,  # TODO: ML model in V2
                umbral_configurado=umbral_alerta
            )
            db.add(prediccion)
        else:
            # Update existing
            prediccion.km_actual = vehiculo.odometro_actual
            prediccion.km_proximo_pm = km_proximo_pm
            prediccion.fecha_proximo_pm = fecha_proximo_pm
            prediccion.dias_hasta_pm = dias_hasta_pm
            prediccion.updated_at = datetime.utcnow()
        
        db.flush()
        return prediccion
    
    @staticmethod
    def check_pm_threshold_and_alert(db: Session, vehiculo_id: UUID):
        """Check if vehicle is approaching PM threshold and create alert if needed."""
        vehiculo = db.query(Vehiculo).filter(Vehiculo.id == vehiculo_id).first()
        if not vehiculo:
            return
        
        prediccion = db.query(PrediccionPM).filter(
            PrediccionPM.vehiculo_id == vehiculo_id
        ).order_by(desc(PrediccionPM.created_at)).first()
        
        if not prediccion:
            prediccion = PredictionService.calculate_next_pm(db, vehiculo_id)
            if not prediccion:
                return
        
        # Calculate progress towards PM
        km_desde_ultimo_calculo = vehiculo.odometro_actual - prediccion.km_actual
        km_hasta_pm = prediccion.km_proximo_pm - vehiculo.odometro_actual
        
        if km_hasta_pm <= 0:
            # PM vencido
            progreso = 1.0
        else:
            progreso = 1.0 - (km_hasta_pm / (prediccion.km_proximo_pm - prediccion.km_actual))
        
        umbral = float(prediccion.umbral_configurado or 0.90)
        
        if progreso >= umbral:
            # Check if alert already exists
            from app.models.alert import AlertaPredictiva
            existing_alert = db.query(AlertaPredictiva).filter(
                AlertaPredictiva.vehiculo_id == vehiculo_id,
                AlertaPredictiva.tipo == "PM_PROXIMA",
                AlertaPredictiva.estado == "PENDIENTE"
            ).first()
            
            if not existing_alert:
                alert_service = AlertService(db)
                alert_service.create_predictive_alert(
                    vehiculo_id=vehiculo_id,
                    tipo="PM_PROXIMA",
                    mensaje=f"PM próximo para vehículo {vehiculo.placa}: {km_hasta_pm} km restantes",
                    criticidad="MEDIA" if progreso < 1.0 else "ALTA",
                    metadata={
                        "km_hasta_pm": km_hasta_pm,
                        "progreso": progreso,
                        "fecha_estimada": str(prediccion.fecha_proximo_pm)
                    }
                )
    
    @staticmethod
    def get_severidad_reciente(db: Session, vehiculo_id: UUID, dias: int = 30) -> str:
        """Get recent severity of use for a vehicle."""
        fecha_limite = date.today() - timedelta(days=dias)
        
        # Count severe usage days
        dias_severos = db.query(func.count(SeveridadUso.id)).filter(
            SeveridadUso.vehiculo_id == vehiculo_id,
            SeveridadUso.fecha >= fecha_limite,
            SeveridadUso.tipo_uso == "SEVERO"
        ).scalar() or 0
        
        # If more than 40% of days are severe, classify as SEVERO
        if dias_severos > (dias * 0.4):
            return "SEVERO"
        
        return "NORMAL"
    
    @staticmethod
    def estimate_avg_km_per_day(db: Session, vehiculo_id: UUID, dias: int = 30) -> float:
        """Estimate average km per day for a vehicle."""
        fecha_limite = date.today() - timedelta(days=dias)
        
        km_total = db.query(func.sum(SeveridadUso.km_recorridos)).filter(
            SeveridadUso.vehiculo_id == vehiculo_id,
            SeveridadUso.fecha >= fecha_limite
        ).scalar() or 0
        
        dias_con_datos = db.query(func.count(SeveridadUso.id)).filter(
            SeveridadUso.vehiculo_id == vehiculo_id,
            SeveridadUso.fecha >= fecha_limite
        ).scalar() or 1
        
        return km_total / max(dias_con_datos, 1)
    
    @staticmethod
    def recalculate_severity_and_predictions(db: Session, vehiculo_id: UUID):
        """Recalculate severity of use and PM predictions for a vehicle."""
        # Recalculate severity for last 30 days
        fecha_30d = date.today() - timedelta(days=30)
        
        severidades = db.query(SeveridadUso).filter(
            SeveridadUso.vehiculo_id == vehiculo_id,
            SeveridadUso.fecha >= fecha_30d
        ).all()
        
        for sev in severidades:
            # Count driving events for that day
            eventos = db.query(EventoConducta).filter(
                EventoConducta.vehiculo_id == vehiculo_id,
                func.date(EventoConducta.timestamp) == sev.fecha
            ).all()
            
            frenazos = sum(1 for e in eventos if e.tipo_evento == "FRENAZO")
            exceso_vel = sum(1 for e in eventos if e.tipo_evento == "EXCESO_VELOCIDAD")
            
            sev.eventos_frenazos = frenazos
            sev.eventos_exceso_vel = exceso_vel
            
            # Classify as severe if excessive events
            if frenazos > 80 or exceso_vel > 10:
                sev.tipo_uso = "SEVERO"
            else:
                sev.tipo_uso = "NORMAL"
        
        # Recalculate PM prediction
        PredictionService.calculate_next_pm(db, vehiculo_id)
        
        # Check if alert needed
        PredictionService.check_pm_threshold_and_alert(db, vehiculo_id)
        
        db.flush()

