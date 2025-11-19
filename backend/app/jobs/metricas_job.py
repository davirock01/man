"""
Job to calculate KPIs and metrics.
Runs daily.
"""
import asyncio
from datetime import datetime, timedelta
from sqlalchemy import select, func, and_

from app.core.database import AsyncSessionLocal
from app.models.vehiculo import Vehiculo
from app.models.dvir import DVIR
from app.models.orden_trabajo import OrdenTrabajo, MetricasEjecucion
from app.models.salud_vehiculo import PrediccionPM


async def calculate_metricas():
    """Calculate daily KPIs and metrics."""
    async with AsyncSessionLocal() as db:
        print("Calculating daily metrics...")
        
        # PM Compliance
        result_total = await db.execute(select(func.count(Vehiculo.id)))
        total_vehiculos = result_total.scalar() or 0
        
        result_ok = await db.execute(
            select(func.count(PrediccionPM.vehiculo_id))
            .where(PrediccionPM.alerta_generada == "NO")
        )
        vehiculos_pm_ok = result_ok.scalar() or 0
        
        pm_compliance = (vehiculos_pm_ok / total_vehiculos * 100) if total_vehiculos > 0 else 0
        
        # DVIR Compliance (completed in last 24h)
        fecha_limite = datetime.utcnow() - timedelta(hours=24)
        result_dvirs = await db.execute(
            select(func.count(DVIR.id))
            .where(DVIR.timestamp >= fecha_limite)
        )
        dvirs_24h = result_dvirs.scalar() or 0
        
        # OTs completed in last 24h
        result_ots = await db.execute(
            select(func.count(OrdenTrabajo.id))
            .where(
                and_(
                    OrdenTrabajo.fecha_fin >= fecha_limite,
                    OrdenTrabajo.estado == "COMPLETADA"
                )
            )
        )
        ots_completadas_24h = result_ots.scalar() or 0
        
        # Average OT completion time
        result_metricas = await db.execute(
            select(func.avg(MetricasEjecucion.tiempo_total_min))
            .where(MetricasEjecucion.creado_en >= fecha_limite)
        )
        avg_ot_time = result_metricas.scalar() or 0
        
        print(f"Daily Metrics Summary:")
        print(f"- PM Compliance: {pm_compliance:.1f}%")
        print(f"- DVIRs completed (24h): {dvirs_24h}")
        print(f"- OTs completed (24h): {ots_completadas_24h}")
        print(f"- Avg OT time (24h): {avg_ot_time:.1f} min")
        print(f"- Total vehicles: {total_vehiculos}")
        
        # Store metrics (would create a metrics table in production)
        # For now, just log them
        
        await db.commit()


def run_metricas_job():
    """Entry point for job scheduler."""
    asyncio.run(calculate_metricas())


if __name__ == "__main__":
    run_metricas_job()


