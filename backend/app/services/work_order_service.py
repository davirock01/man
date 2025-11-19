from sqlalchemy.orm import Session
from sqlalchemy import func, desc
from uuid import UUID
from typing import Dict, Any, List, Optional
from datetime import datetime, timedelta

from app.models.work_order import OrdenWork, OrdenWorkItem, OrdenWorkLog
from app.models.dvir import DVIR
from app.models.patron_recurrente import PatronRecurrente
from app.models.evento_conducta import EventoConducta
from app.schemas.work_order import OrdenWorkCreate, OrdenWorkItemCreate


class WorkOrderService:
    def __init__(self, db: Session):
        self.db = db
    
    def create_work_order(self, data: OrdenWorkCreate, coordinador_id: UUID) -> OrdenWork:
        """Create a new work order with context."""
        # Generate context for OT
        contexto = self.generate_context_for_ot(data.vehiculo_id, data.tipo)
        
        # Create work order
        orden = OrdenWork(
            vehiculo_id=data.vehiculo_id,
            tipo=data.tipo,
            prioridad=data.prioridad,
            descripcion=data.descripcion,
            fecha_programada=data.fecha_programada,
            tecnico_id=data.tecnico_id,
            coordinador_id=coordinador_id,
            duracion_estimada_min=data.duracion_estimada_min or contexto.get("duracion_estimada_min"),
            costo_estimado=data.costo_estimado,
            contexto_json=contexto,
            estado="ASIGNADA" if data.tecnico_id else "PENDIENTE"
        )
        
        if data.tecnico_id:
            orden.fecha_asignacion = datetime.utcnow()
        
        self.db.add(orden)
        self.db.flush()
        
        # Create work order items
        for item_data in data.items:
            item = OrdenWorkItem(
                ot_id=orden.id,
                tarea=item_data.tarea,
                tiempo_estimado_min=item_data.tiempo_estimado_min
            )
            self.db.add(item)
        
        # Log creation
        log = OrdenWorkLog(
            ot_id=orden.id,
            evento="CREADA",
            usuario_id=coordinador_id,
            payload_json={"tipo": data.tipo, "prioridad": data.prioridad}
        )
        self.db.add(log)
        
        self.db.flush()
        return orden
    
    def generate_context_for_ot(self, vehiculo_id: UUID, tipo_ot: str) -> Dict[str, Any]:
        """
        Generate context information for a work order.
        Includes historical data, patterns, suggested parts, etc.
        """
        from app.services.prediction_service import PredictionService
        
        contexto = {}
        
        # Last 10 DVIRs
        dvirs = self.db.query(DVIR).filter(
            DVIR.vehiculo_id == vehiculo_id
        ).order_by(desc(DVIR.timestamp)).limit(10).all()
        
        contexto["historial_dvir"] = [
            {
                "id": str(d.id),
                "timestamp": d.timestamp.isoformat(),
                "estado_resumen": d.estado_resumen,
                "odometro": d.odometro
            }
            for d in dvirs
        ]
        
        # Active patterns
        patrones = self.db.query(PatronRecurrente).filter(
            PatronRecurrente.vehiculo_id == vehiculo_id,
            PatronRecurrente.estado == "ACTIVO"
        ).all()
        
        contexto["patrones"] = [
            {
                "componente": p.componente,
                "veces_30d": p.veces_30d,
                "criticidad": p.criticidad
            }
            for p in patrones
        ]
        
        # Driving events count (last 30 days)
        fecha_30d = datetime.utcnow() - timedelta(days=30)
        eventos_count = self.db.query(func.count(EventoConducta.id)).filter(
            EventoConducta.vehiculo_id == vehiculo_id,
            EventoConducta.timestamp >= fecha_30d
        ).scalar() or 0
        
        contexto["eventos_conducta"] = eventos_count
        
        # Severity of use
        severidad_uso = PredictionService.get_severidad_reciente(self.db, vehiculo_id)
        contexto["severidad_uso"] = severidad_uso
        
        # Similar historical OTs
        ots_similares = self.db.query(OrdenWork).filter(
            OrdenWork.vehiculo_id == vehiculo_id,
            OrdenWork.tipo == tipo_ot,
            OrdenWork.estado == "COMPLETADA"
        ).order_by(desc(OrdenWork.fecha_fin)).limit(5).all()
        
        if ots_similares:
            duraciones = [ot.duracion_real_min for ot in ots_similares if ot.duracion_real_min]
            if duraciones:
                contexto["duracion_estimada_min"] = int(sum(duraciones) / len(duraciones))
                contexto["ot_similares_count"] = len(ots_similares)
        
        # Suggested parts (placeholder for V2 - ML model)
        contexto["repuestos_sugeridos"] = self._suggest_parts(vehiculo_id, tipo_ot, patrones)
        
        return contexto
    
    def _suggest_parts(self, vehiculo_id: UUID, tipo_ot: str, patrones: List) -> List[Dict]:
        """Suggest parts based on OT type and patterns (basic heuristic)."""
        sugerencias = []
        
        if tipo_ot == "PM_PREVENTIVO":
            sugerencias = [
                {"sku": "OIL-001", "descripcion": "Aceite motor", "cantidad": 1},
                {"sku": "FILTER-001", "descripcion": "Filtro aceite", "cantidad": 1},
                {"sku": "FILTER-002", "descripcion": "Filtro aire", "cantidad": 1}
            ]
        
        # Add parts based on recurrent patterns
        for patron in patrones:
            if "Frenos" in patron.componente:
                sugerencias.append({
                    "sku": "BRK-001",
                    "descripcion": "Pastillas de freno",
                    "cantidad": 1,
                    "razon": f"Patrón recurrente: {patron.componente}"
                })
            elif "Luces" in patron.componente:
                sugerencias.append({
                    "sku": "LIGHT-001",
                    "descripcion": "Foco delantero",
                    "cantidad": 2,
                    "razon": f"Patrón recurrente: {patron.componente}"
                })
        
        return sugerencias
    
    def check_ot_overtime(self, ot_id: UUID) -> Optional[Dict]:
        """Check if OT is overtime and return alert if needed."""
        ot = self.db.query(OrdenWork).filter(OrdenWork.id == ot_id).first()
        
        if not ot or not ot.fecha_inicio or ot.estado != "EN_PROGRESO":
            return None
        
        if not ot.duracion_estimada_min:
            return None
        
        duracion_actual_min = (datetime.utcnow() - ot.fecha_inicio).total_seconds() / 60
        duracion_estimada = ot.duracion_estimada_min
        
        desviacion_pct = (duracion_actual_min - duracion_estimada) / duracion_estimada
        
        # Check if already alerted for this threshold
        logs = self.db.query(OrdenWorkLog).filter(
            OrdenWorkLog.ot_id == ot_id,
            OrdenWorkLog.evento.in_(["ALERTA_SOBRETIEMPO_20", "ALERTA_SOBRETIEMPO_50"])
        ).all()
        
        alerted_50 = any(log.evento == "ALERTA_SOBRETIEMPO_50" for log in logs)
        alerted_20 = any(log.evento == "ALERTA_SOBRETIEMPO_20" for log in logs)
        
        if desviacion_pct > 0.50 and not alerted_50:
            # Log alert
            log = OrdenWorkLog(
                ot_id=ot_id,
                evento="ALERTA_SOBRETIEMPO_50",
                payload_json={"desviacion_pct": desviacion_pct}
            )
            self.db.add(log)
            self.db.flush()
            
            return {
                "ot_id": str(ot_id),
                "tipo": "SOBRETIEMPO_50",
                "criticidad": "ALTA",
                "mensaje": f"OT {ot_id} con sobretiempo del 50%"
            }
        elif desviacion_pct > 0.20 and not alerted_20:
            # Log alert
            log = OrdenWorkLog(
                ot_id=ot_id,
                evento="ALERTA_SOBRETIEMPO_20",
                payload_json={"desviacion_pct": desviacion_pct}
            )
            self.db.add(log)
            self.db.flush()
            
            return {
                "ot_id": str(ot_id),
                "tipo": "SOBRETIEMPO_20",
                "criticidad": "MEDIA",
                "mensaje": f"OT {ot_id} con sobretiempo del 20%"
            }
        
        return None

