"""
Job to process driving events and update severity of use.
Runs every 10 minutes.
"""
import asyncio
from datetime import datetime, timedelta
from sqlalchemy import select, func
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.database import AsyncSessionLocal
from app.models.vehiculo import Vehiculo
from app.models.dvir import EventoConducta, SeveridadUso


async def process_eventos_conducta():
    """Process driving events and update severity of use for all vehicles."""
    async with AsyncSessionLocal() as db:
        # Get all active vehicles
        result = await db.execute(
            select(Vehiculo).where(Vehiculo.estado_operativo != "FUERA_SERVICIO")
        )
        vehiculos = result.scalars().all()
        
        for vehiculo in vehiculos:
            await _process_vehicle_eventos(db, vehiculo.id)
        
        await db.commit()


async def _process_vehicle_eventos(db: AsyncSession, vehiculo_id: int):
    """Process driving events for a single vehicle."""
    # Get events from last 24 hours
    fecha_limite = datetime.utcnow() - timedelta(hours=24)
    
    result = await db.execute(
        select(EventoConducta)
        .where(
            EventoConducta.vehiculo_id == vehiculo_id,
            EventoConducta.timestamp >= fecha_limite
        )
    )
    eventos = result.scalars().all()
    
    if not eventos:
        return
    
    # Count events by severity
    eventos_severos = len([e for e in eventos if e.severidad == "SEVERO"])
    eventos_moderados = len([e for e in eventos if e.severidad == "MODERADO"])
    eventos_leves = len([e for e in eventos if e.severidad == "LEVE"])
    
    # Calculate severity score
    score_severidad = (eventos_severos * 10 + eventos_moderados * 5 + eventos_leves * 1)
    
    # Determine uso type
    if score_severidad >= 50:
        tipo_uso = "SEVERO"
    elif score_severidad >= 20:
        tipo_uso = "MODERADO"
    else:
        tipo_uso = "NORMAL"
    
    # Create or update severidad_uso record
    severidad = SeveridadUso(
        vehiculo_id=vehiculo_id,
        fecha=datetime.utcnow(),
        tipo_uso=tipo_uso,
        score_severidad=float(score_severidad),
        metricas_json={
            "eventos_severos": eventos_severos,
            "eventos_moderados": eventos_moderados,
            "eventos_leves": eventos_leves,
            "total_eventos": len(eventos),
            "periodo_horas": 24,
        }
    )
    
    db.add(severidad)


def run_eventos_conducta_job():
    """Entry point for job scheduler."""
    asyncio.run(process_eventos_conducta())


if __name__ == "__main__":
    run_eventos_conducta_job()


