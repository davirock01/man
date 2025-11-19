"""
Job to check OT overtime and generate alerts.
Runs every 5 minutes.
"""
import asyncio
from sqlalchemy import select

from app.core.database import AsyncSessionLocal
from app.models.orden_trabajo import OrdenTrabajo
from app.services.orden_trabajo_service import OrdenTrabajoService


async def check_ot_overtime():
    """Check overtime for all in-progress work orders."""
    async with AsyncSessionLocal() as db:
        # Get all in-progress OTs
        result = await db.execute(
            select(OrdenTrabajo)
            .where(OrdenTrabajo.estado == "EN_PROGRESO")
        )
        ots = result.scalars().all()
        
        service = OrdenTrabajoService(db)
        
        for ot in ots:
            try:
                await service.check_ot_overtime(ot.id)
            except Exception as e:
                print(f"Error checking overtime for OT {ot.id}: {e}")
        
        await db.commit()
        print(f"OT overtime checked for {len(ots)} work orders")


def run_ot_timer_job():
    """Entry point for job scheduler."""
    asyncio.run(check_ot_overtime())


if __name__ == "__main__":
    run_ot_timer_job()


