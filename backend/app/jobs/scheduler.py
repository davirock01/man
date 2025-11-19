"""
Job scheduler configuration using APScheduler.
"""
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.triggers.cron import CronTrigger
from apscheduler.triggers.interval import IntervalTrigger

from app.jobs.eventos_conducta_job import run_eventos_conducta_job
from app.jobs.recalculo_salud_job import run_recalculo_salud_job
from app.jobs.alertas_pm_job import run_alertas_pm_job
from app.jobs.patrones_job import run_patrones_job
from app.jobs.ot_timer_job import run_ot_timer_job
from app.jobs.metricas_job import run_metricas_job


def setup_scheduler():
    """Setup and configure the job scheduler."""
    scheduler = AsyncIOScheduler()
    
    # EventosConductaJob - every 10 minutes
    scheduler.add_job(
        run_eventos_conducta_job,
        trigger=IntervalTrigger(minutes=10),
        id="eventos_conducta_job",
        name="Process driving events",
        replace_existing=True,
    )
    
    # RecalculoSaludJob - daily at 1 AM
    scheduler.add_job(
        run_recalculo_salud_job,
        trigger=CronTrigger(hour=1, minute=0),
        id="recalculo_salud_job",
        name="Recalculate fleet health scores",
        replace_existing=True,
    )
    
    # AlertasPMJob - hourly
    scheduler.add_job(
        run_alertas_pm_job,
        trigger=IntervalTrigger(hours=1),
        id="alertas_pm_job",
        name="Check PM thresholds",
        replace_existing=True,
    )
    
    # PatronesJob - daily at 2 AM
    scheduler.add_job(
        run_patrones_job,
        trigger=CronTrigger(hour=2, minute=0),
        id="patrones_job",
        name="Detect recurring patterns",
        replace_existing=True,
    )
    
    # OTTimerJob - every 5 minutes
    scheduler.add_job(
        run_ot_timer_job,
        trigger=IntervalTrigger(minutes=5),
        id="ot_timer_job",
        name="Check OT overtime",
        replace_existing=True,
    )
    
    # MetricasJob - daily at 3 AM
    scheduler.add_job(
        run_metricas_job,
        trigger=CronTrigger(hour=3, minute=0),
        id="metricas_job",
        name="Calculate daily metrics",
        replace_existing=True,
    )
    
    return scheduler


def start_scheduler():
    """Start the job scheduler."""
    scheduler = setup_scheduler()
    scheduler.start()
    print("Job scheduler started successfully")
    return scheduler


