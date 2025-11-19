"""
Job to detect recurring patterns in DVIR defects.
Runs daily.
"""
import asyncio
from sqlalchemy import select

from app.core.database import AsyncSessionLocal
from app.models.vehiculo import Vehiculo
from app.services.alert_service import AlertService


async def detectar_patrones():
    """Detect recurring patterns for all vehicles."""
    async with AsyncSessionLocal() as db:
        # Get all active vehicles
        result = await db.execute(
            select(Vehiculo).where(Vehiculo.estado_operativo != "FUERA_SERVICIO")
        )
        vehiculos = result.scalars().all()
        
        service = AlertService(db)
        
        total_patrones = 0
        for vehiculo in vehiculos:
            try:
                patrones = await service.check_recurring_patterns(vehiculo.id)
                if patrones:
                    total_patrones += len(patrones)
                    print(f"Detected {len(patrones)} patterns for vehicle {vehiculo.placa}")
            except Exception as e:
                print(f"Error detecting patterns for vehicle {vehiculo.placa}: {e}")
        
        await db.commit()
        print(f"Pattern detection completed: {total_patrones} total patterns found")


def run_patrones_job():
    """Entry point for job scheduler."""
    asyncio.run(detectar_patrones())


if __name__ == "__main__":
    run_patrones_job()


