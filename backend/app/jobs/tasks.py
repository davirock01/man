from datetime import datetime, timedelta, date
from sqlalchemy import func
from app.jobs.celery_app import celery_app
from app.core.database import SessionLocal
from app.models.vehiculo import Vehiculo
from app.models.evento_conducta import EventoConducta
from app.models.severidad_uso import SeveridadUso
from app.models.work_order import OrdenWork
from app.models.alert import AlertaPredictiva, AlertaReactiva
from app.services.health_score_service import HealthScoreService
from app.services.prediction_service import PredictionService
from app.services.pattern_service import PatternDetectionService
from app.services.alert_service import AlertService
from app.services.work_order_service import WorkOrderService
import random


@celery_app.task(name='app.jobs.tasks.update_driving_events')
def update_driving_events():
    """
    Simulates receiving data from GPS/telematics devices.
    In production, this would integrate with actual telematics API.
    """
    db = SessionLocal()
    try:
        # Get vehicles currently in operation (simplified)
        vehiculos_activos = db.query(Vehiculo).filter(
            Vehiculo.estado_operativo == "OPERATIVO"
        ).all()
        
        eventos_creados = 0
        
        for vehiculo in vehiculos_activos:
            # Simulate GPS/telematics data (in production, fetch from device API)
            # For demonstration, randomly generate some events
            if random.random() < 0.3:  # 30% chance of event
                tipo_evento = random.choice(["FRENAZO", "EXCESO_VELOCIDAD", "ACELERACION_BRUSCA"])
                severidad = random.randint(1, 10)
                
                evento = EventoConducta(
                    vehiculo_id=vehiculo.id,
                    conductor_id=None,  # Would be set from GPS device data
                    tipo_evento=tipo_evento,
                    severidad=severidad,
                    gps_lat=vehiculo.ultima_lat,
                    gps_lng=vehiculo.ultima_lng
                )
                db.add(evento)
                eventos_creados += 1
            
            # Recalculate severity of use for today
            hoy = date.today()
            severidad = db.query(SeveridadUso).filter(
                SeveridadUso.vehiculo_id == vehiculo.id,
                SeveridadUso.fecha == hoy
            ).first()
            
            # Count events today
            eventos_hoy = db.query(EventoConducta).filter(
                EventoConducta.vehiculo_id == vehiculo.id,
                func.date(EventoConducta.timestamp) == hoy
            ).all()
            
            frenazos = sum(1 for e in eventos_hoy if e.tipo_evento == "FRENAZO")
            exceso_vel = sum(1 for e in eventos_hoy if e.tipo_evento == "EXCESO_VELOCIDAD")
            
            if severidad:
                severidad.eventos_frenazos = frenazos
                severidad.eventos_exceso_vel = exceso_vel
                severidad.tipo_uso = "SEVERO" if frenazos > 80 or exceso_vel > 10 else "NORMAL"
            else:
                severidad = SeveridadUso(
                    vehiculo_id=vehiculo.id,
                    fecha=hoy,
                    eventos_frenazos=frenazos,
                    eventos_exceso_vel=exceso_vel,
                    tipo_uso="SEVERO" if frenazos > 80 or exceso_vel > 10 else "NORMAL"
                )
                db.add(severidad)
        
        db.commit()
        print(f"[Job] Eventos de conducción actualizados: {eventos_creados} eventos creados")
        return {"eventos_creados": eventos_creados}
        
    except Exception as e:
        db.rollback()
        print(f"[Job] Error actualizando eventos de conducción: {str(e)}")
        raise
    finally:
        db.close()


@celery_app.task(name='app.jobs.tasks.recalculate_health_scores')
def recalculate_health_scores():
    """Calculate health scores for all active vehicles."""
    db = SessionLocal()
    try:
        vehiculos = db.query(Vehiculo).filter(
            Vehiculo.estado_operativo.in_(["OPERATIVO", "NO_OPERATIVO", "EN_MANTENIMIENTO"])
        ).all()
        
        actualizados = 0
        
        for vehiculo in vehiculos:
            try:
                HealthScoreService.calculate_and_save(db, vehiculo.id)
                actualizados += 1
            except Exception as e:
                print(f"[Job] Error calculando score para vehículo {vehiculo.placa}: {str(e)}")
                continue
        
        db.commit()
        print(f"[Job] Scores de salud actualizados: {actualizados} vehículos")
        return {"vehiculos_actualizados": actualizados}
        
    except Exception as e:
        db.rollback()
        print(f"[Job] Error recalculando scores de salud: {str(e)}")
        raise
    finally:
        db.close()


@celery_app.task(name='app.jobs.tasks.check_pm_thresholds')
def check_pm_thresholds():
    """Check PM thresholds and generate alerts for vehicles approaching maintenance."""
    db = SessionLocal()
    try:
        vehiculos = db.query(Vehiculo).all()
        
        alertas_generadas = 0
        
        for vehiculo in vehiculos:
            try:
                # Calculate next PM
                prediccion = PredictionService.calculate_next_pm(db, vehiculo.id)
                
                # Check if alert needed
                PredictionService.check_pm_threshold_and_alert(db, vehiculo.id)
                
                alertas_generadas += 1
            except Exception as e:
                print(f"[Job] Error verificando PM para vehículo {vehiculo.placa}: {str(e)}")
                continue
        
        db.commit()
        print(f"[Job] Umbrales PM verificados: {alertas_generadas} vehículos procesados")
        return {"vehiculos_procesados": alertas_generadas}
        
    except Exception as e:
        db.rollback()
        print(f"[Job] Error verificando umbrales PM: {str(e)}")
        raise
    finally:
        db.close()


@celery_app.task(name='app.jobs.tasks.detect_recurrent_patterns')
def detect_recurrent_patterns():
    """Detect recurrent defect patterns across all vehicles."""
    db = SessionLocal()
    try:
        vehiculos = db.query(Vehiculo).all()
        
        patrones_detectados = 0
        
        for vehiculo in vehiculos:
            try:
                pattern_service = PatternDetectionService(db)
                patrones = pattern_service.scan_recurrent_defects(vehiculo.id, dias=30)
                
                alert_service = AlertService(db)
                
                for patron in patrones:
                    # Check if pattern already exists
                    from app.models.patron_recurrente import PatronRecurrente
                    existing = db.query(PatronRecurrente).filter(
                        PatronRecurrente.vehiculo_id == vehiculo.id,
                        PatronRecurrente.componente == patron.componente,
                        PatronRecurrente.estado == "ACTIVO"
                    ).first()
                    
                    if not existing:
                        db.add(patron)
                        alert_service.create_predictive_alert(
                            vehiculo_id=vehiculo.id,
                            tipo="PATRON_RECURRENTE",
                            mensaje=f"Patrón recurrente detectado: {patron.componente} ha fallado {patron.veces_30d} veces en 30 días",
                            criticidad="MEDIA"
                        )
                        patrones_detectados += 1
                
            except Exception as e:
                print(f"[Job] Error detectando patrones para vehículo {vehiculo.placa}: {str(e)}")
                continue
        
        db.commit()
        print(f"[Job] Patrones recurrentes detectados: {patrones_detectados} nuevos patrones")
        return {"patrones_detectados": patrones_detectados}
        
    except Exception as e:
        db.rollback()
        print(f"[Job] Error detectando patrones recurrentes: {str(e)}")
        raise
    finally:
        db.close()


@celery_app.task(name='app.jobs.tasks.monitor_ot_timers')
def monitor_ot_timers():
    """Monitor work order timers and generate alerts for overtime."""
    db = SessionLocal()
    try:
        ots_en_progreso = db.query(OrdenWork).filter(
            OrdenWork.estado == "EN_PROGRESO"
        ).all()
        
        alertas_generadas = 0
        work_order_service = WorkOrderService(db)
        alert_service = AlertService(db)
        
        for ot in ots_en_progreso:
            try:
                alert_data = work_order_service.check_ot_overtime(ot.id)
                
                if alert_data:
                    # Create system alert for coordinators
                    alert_service.create_reactive_alert(
                        vehiculo_id=ot.vehiculo_id,
                        origen="SISTEMA",
                        mensaje=alert_data["mensaje"],
                        criticidad=alert_data["criticidad"],
                        metadata={"ot_id": str(ot.id), "tipo": alert_data["tipo"]}
                    )
                    alertas_generadas += 1
                    
            except Exception as e:
                print(f"[Job] Error monitoreando OT {ot.id}: {str(e)}")
                continue
        
        db.commit()
        print(f"[Job] Cronómetros OT monitoreados: {alertas_generadas} alertas generadas")
        return {"alertas_generadas": alertas_generadas}
        
    except Exception as e:
        db.rollback()
        print(f"[Job] Error monitoreando cronómetros OT: {str(e)}")
        raise
    finally:
        db.close()


@celery_app.task(name='app.jobs.tasks.cleanup_old_alerts')
def cleanup_old_alerts():
    """Archive or delete old resolved alerts."""
    db = SessionLocal()
    try:
        fecha_limite = datetime.utcnow() - timedelta(days=90)
        
        # Delete old resolved predictive alerts
        deleted_predictive = db.query(AlertaPredictiva).filter(
            AlertaPredictiva.estado == "RESUELTA",
            AlertaPredictiva.resuelta_en < fecha_limite
        ).delete()
        
        # Delete old resolved reactive alerts
        deleted_reactive = db.query(AlertaReactiva).filter(
            AlertaReactiva.estado == "RESUELTA",
            AlertaReactiva.resuelta_en < fecha_limite
        ).delete()
        
        db.commit()
        
        total_deleted = deleted_predictive + deleted_reactive
        print(f"[Job] Alertas antiguas limpiadas: {total_deleted} eliminadas")
        return {
            "deleted_predictive": deleted_predictive,
            "deleted_reactive": deleted_reactive,
            "total": total_deleted
        }
        
    except Exception as e:
        db.rollback()
        print(f"[Job] Error limpiando alertas antiguas: {str(e)}")
        raise
    finally:
        db.close()

