"""
Job to recalculate health scores for all vehicles.
Runs daily.
"""
import asyncio
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.database import AsyncSessionLocal
from app.models.vehiculo import Vehiculo
from app.services.salud_vehiculo_service import SaludVehiculoService


async def recalcular_salud_flota():
    """Recalculate health scores for all vehicles in the fleet."""
    async with AsyncSessionLocal() as db:
        # Get all active vehicles
        result = await db.execute(
            select(Vehiculo).where(Vehiculo.estado_operativo != "FUERA_SERVICIO")
        )
        vehiculos = result.scalars().all()
        
        service = SaludVehiculoService(db)
        
        for vehiculo in vehiculos:
            try:
                await service.calculate_health_score(vehiculo.id)
                print(f"Health score recalculated for vehicle {vehiculo.placa}")
            except Exception as e:
                print(f"Error calculating health for vehicle {vehiculo.placa}: {e}")
        
        await db.commit()
        print(f"Health recalculation completed for {len(vehiculos)} vehicles")


def run_recalculo_salud_job():
    """Entry point for job scheduler."""
    asyncio.run(recalcular_salud_flota())


if __name__ == "__main__":
    run_recalculo_salud_job()


