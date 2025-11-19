"""
Job to check PM thresholds and generate predictive alerts.
Runs hourly.
"""
import asyncio
from sqlalchemy import select

from app.core.database import AsyncSessionLocal
from app.models.vehiculo import Vehiculo
from app.services.prediccion_pm_service import PrediccionPMService


async def check_alertas_pm():
    """Check PM thresholds for all vehicles and generate alerts if needed."""
    async with AsyncSessionLocal() as db:
        # Get all active vehicles
        result = await db.execute(
            select(Vehiculo).where(Vehiculo.estado_operativo != "FUERA_SERVICIO")
        )
        vehiculos = result.scalars().all()
        
        service = PrediccionPMService(db)
        
        for vehiculo in vehiculos:
            try:
                await service.check_pm_threshold(vehiculo.id)
                print(f"PM threshold checked for vehicle {vehiculo.placa}")
            except Exception as e:
                print(f"Error checking PM for vehicle {vehiculo.placa}: {e}")
        
        await db.commit()
        print(f"PM alerts checked for {len(vehiculos)} vehicles")


def run_alertas_pm_job():
    """Entry point for job scheduler."""
    asyncio.run(check_alertas_pm())


if __name__ == "__main__":
    run_alertas_pm_job()


