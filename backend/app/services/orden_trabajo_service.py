from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, update
from datetime import datetime, timedelta
from typing import Optional, Dict, Any

from app.models.orden_trabajo import OrdenTrabajo, OrdenTrabajoItem, OrdenTrabajoLog, MetricasEjecucion
from app.models.dvir import DVIR
from app.models.alerta import AlertaReactiva, AlertaPredictiva, PatronRecurrente
from app.schemas.orden_trabajo import OrdenTrabajoCreate
from app.core.config import settings


class OrdenTrabajoService:
    """Service for work order operations."""
    
    def __init__(self, db: AsyncSession):
        self.db = db
    
    async def create_ot_from_alert(
        self,
        alerta_id: int,
        alerta_tipo: str,
        coordinador_id: int,
    ) -> OrdenTrabajo:
        """
        Create a work order from an alert (reactive or predictive).
        """
        # Get alert details
        if alerta_tipo == "REACTIVA":
            result = await self.db.execute(
                select(AlertaReactiva).where(AlertaReactiva.id == alerta_id)
            )
            alerta = result.scalar_one_or_none()
        else:  # PREDICTIVA
            result = await self.db.execute(
                select(AlertaPredictiva).where(AlertaPredictiva.id == alerta_id)
            )
            alerta = result.scalar_one_or_none()
        
        if not alerta:
            raise ValueError(f"Alert {alerta_id} not found")
        
        # Determine OT type and priority based on alert
        if alerta_tipo == "REACTIVA":
            tipo = "CORRECTIVO" if alerta.criticidad in ["ALTA", "CRITICA"] else "DIAGNOSTICO"
            prioridad = "URGENTE" if alerta.criticidad == "CRITICA" else "ALTA"
            descripcion = f"Atención a alerta reactiva: {alerta.mensaje}"
        else:
            tipo = "PM_PREVENTIVO"
            prioridad = "MEDIA" if alerta.criticidad == "MEDIA" else "ALTA"
            descripcion = f"Mantenimiento preventivo: {alerta.mensaje}"
        
        # Generate context
        contexto = await self.generate_ot_context(alerta.vehiculo_id)
        
        # Create OT
        ot = OrdenTrabajo(
            vehiculo_id=alerta.vehiculo_id,
            tipo=tipo,
            prioridad=prioridad,
            estado="PENDIENTE",
            coordinador_id=coordinador_id,
            descripcion=descripcion,
            contexto_json=contexto,
            origen_alerta_id=alerta_id,
            origen_tipo=f"ALERTA_{alerta_tipo}",
            duracion_estimada_min=contexto.get("duracion_estimada_min"),
        )
        
        self.db.add(ot)
        await self.db.commit()
        await self.db.refresh(ot)
        
        # Log creation
        await self._log_event(ot.id, "CREADA", coordinador_id, {
            "origen": f"ALERTA_{alerta_tipo}",
            "alerta_id": alerta_id,
        })
        
        return ot
    
    async def generate_ot_context(self, vehiculo_id: int) -> Dict[str, Any]:
        """
        Generate historical context for an OT.
        
        Includes:
        - Recent DVIRs
        - Similar past OTs
        - Recurring patterns
        - Suggested parts
        - Estimated duration
        """
        context = {
            "vehiculo_id": vehiculo_id,
            "generado_en": datetime.utcnow().isoformat(),
        }
        
        # Get last 5 DVIRs
        result = await self.db.execute(
            select(DVIR)
            .where(DVIR.vehiculo_id == vehiculo_id)
            .order_by(DVIR.timestamp.desc())
            .limit(5)
        )
        dvirs = result.scalars().all()
        context["dvirs_recientes"] = [
            {
                "id": d.id,
                "fecha": d.timestamp.isoformat(),
                "estado": d.estado_resumen,
            }
            for d in dvirs
        ]
        
        # Get similar past OTs
        result = await self.db.execute(
            select(OrdenTrabajo)
            .where(
                OrdenTrabajo.vehiculo_id == vehiculo_id,
                OrdenTrabajo.estado == "COMPLETADA"
            )
            .order_by(OrdenTrabajo.fecha_fin.desc())
            .limit(5)
        )
        ots_pasadas = result.scalars().all()
        
        if ots_pasadas:
            # Calculate average duration
            duraciones = [
                (ot.fecha_fin - ot.fecha_inicio).total_seconds() / 60
                for ot in ots_pasadas
                if ot.fecha_inicio and ot.fecha_fin
            ]
            if duraciones:
                context["duracion_estimada_min"] = int(sum(duraciones) / len(duraciones))
            
            context["ots_similares"] = [
                {
                    "id": ot.id,
                    "tipo": ot.tipo,
                    "duracion_min": (ot.fecha_fin - ot.fecha_inicio).total_seconds() / 60 if ot.fecha_inicio and ot.fecha_fin else None,
                }
                for ot in ots_pasadas
            ]
        
        # Get recurring patterns
        result = await self.db.execute(
            select(PatronRecurrente)
            .where(
                PatronRecurrente.vehiculo_id == vehiculo_id,
                PatronRecurrente.estado == "ACTIVO"
            )
        )
        patrones = result.scalars().all()
        
        if patrones:
            context["patrones_recurrentes"] = [
                {
                    "componente": p.componente,
                    "tipo_defecto": p.tipo_defecto,
                    "veces": p.veces_30d,
                }
                for p in patrones
            ]
        
        # Suggested parts (simplified)
        context["repuestos_sugeridos"] = []
        
        return context
    
    async def start_ot_timer(self, ot_id: int, tecnico_id: int):
        """Start OT timer."""
        await self.db.execute(
            update(OrdenTrabajo)
            .where(OrdenTrabajo.id == ot_id)
            .values(
                estado="EN_PROGRESO",
                fecha_inicio=datetime.utcnow(),
                tecnico_id=tecnico_id,
            )
        )
        
        await self._log_event(ot_id, "INICIADA", tecnico_id, {
            "fecha_inicio": datetime.utcnow().isoformat(),
        })
        
        await self.db.commit()
    
    async def check_ot_overtime(self, ot_id: int):
        """
        Check OT for overtime and generate alerts at 20% and 50% thresholds.
        """
        result = await self.db.execute(
            select(OrdenTrabajo).where(OrdenTrabajo.id == ot_id)
        )
        ot = result.scalar_one_or_none()
        
        if not ot or not ot.fecha_inicio or not ot.duracion_estimada_min:
            return
        
        # Calculate elapsed time
        elapsed_min = (datetime.utcnow() - ot.fecha_inicio).total_seconds() / 60
        estimated_min = ot.duracion_estimada_min
        
        if estimated_min == 0:
            return
        
        overtime_pct = (elapsed_min - estimated_min) / estimated_min
        
        # Check thresholds
        if overtime_pct >= settings.OT_OVERTIME_THRESHOLD_2:  # 50%
            # Generate critical alert
            await self._generate_overtime_alert(ot, "CRITICA", overtime_pct)
        elif overtime_pct >= settings.OT_OVERTIME_THRESHOLD_1:  # 20%
            # Generate moderate alert
            await self._generate_overtime_alert(ot, "MEDIA", overtime_pct)
    
    async def _generate_overtime_alert(self, ot: OrdenTrabajo, criticidad: str, overtime_pct: float):
        """Generate overtime alert for coordinador."""
        from app.services.alert_service import AlertService
        alert_service = AlertService(self.db)
        
        mensaje = f"OT #{ot.id} excede tiempo estimado en {overtime_pct*100:.0f}%"
        
        await alert_service.generate_reactive_alert(
            vehiculo_id=ot.vehiculo_id,
            origen="SISTEMA",
            mensaje=mensaje,
            componente_afectado="OT_TIMER",
            criticidad=criticidad,
        )
    
    async def _log_event(self, ot_id: int, evento: str, usuario_id: Optional[int], payload: Optional[Dict] = None):
        """Log an OT event."""
        log = OrdenTrabajoLog(
            ot_id=ot_id,
            evento=evento,
            usuario_id=usuario_id,
            payload_json=payload or {},
        )
        
        self.db.add(log)
        await self.db.commit()
    
    async def complete_ot(self, ot_id: int, tecnico_id: int):
        """Complete an OT and calculate metrics."""
        # Update OT
        await self.db.execute(
            update(OrdenTrabajo)
            .where(OrdenTrabajo.id == ot_id)
            .values(
                estado="COMPLETADA",
                fecha_fin=datetime.utcnow(),
            )
        )
        
        await self._log_event(ot_id, "COMPLETADA", tecnico_id, {
            "fecha_fin": datetime.utcnow().isoformat(),
        })
        
        # Calculate metrics
        await self._calculate_metrics(ot_id)
        
        await self.db.commit()
    
    async def _calculate_metrics(self, ot_id: int):
        """Calculate execution metrics for completed OT."""
        result = await self.db.execute(
            select(OrdenTrabajo).where(OrdenTrabajo.id == ot_id)
        )
        ot = result.scalar_one_or_none()
        
        if not ot or not ot.fecha_inicio or not ot.fecha_fin:
            return
        
        # Calculate time metrics
        tiempo_total_min = int((ot.fecha_fin - ot.fecha_inicio).total_seconds() / 60)
        tiempo_estimado = ot.duracion_estimada_min or tiempo_total_min
        
        desviacion_tiempo_pct = ((tiempo_total_min - tiempo_estimado) / tiempo_estimado * 100) if tiempo_estimado > 0 else 0
        
        # Get repuestos used
        from app.models.taller import RepuestoUsado
        result = await self.db.execute(
            select(RepuestoUsado).where(RepuestoUsado.ot_id == ot_id)
        )
        repuestos = result.scalars().all()
        
        costo_repuestos = sum(r.costo_total for r in repuestos)
        
        # Create metrics record
        metricas = MetricasEjecucion(
            ot_id=ot_id,
            desviacion_tiempo_pct=desviacion_tiempo_pct,
            tiempo_total_min=tiempo_total_min,
            tiempo_efectivo_min=tiempo_total_min,  # Simplified
            tiempo_pausas_min=0,
            costo_total=costo_repuestos,
            costo_repuestos=costo_repuestos,
            costo_mano_obra=0.0,
            complejidad_final="MEDIA",
            defecto_predicho_confirmado_bool=True,
        )
        
        self.db.add(metricas)
        await self.db.commit()


