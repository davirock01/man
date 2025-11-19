from celery import Celery
from celery.schedules import crontab
from app.core.config import settings

# Create Celery app
celery_app = Celery(
    "fleet_maintenance",
    broker=settings.REDIS_URL,
    backend=settings.REDIS_URL
)

# Celery configuration
celery_app.conf.update(
    task_serializer='json',
    accept_content=['json'],
    result_serializer='json',
    timezone='America/Bogota',
    enable_utc=True,
    task_track_started=True,
    task_time_limit=30 * 60,  # 30 minutes
    worker_prefetch_multiplier=1,
)

# Periodic tasks schedule
celery_app.conf.beat_schedule = {
    'update-driving-events-every-10-minutes': {
        'task': 'app.jobs.tasks.update_driving_events',
        'schedule': 600.0,  # 10 minutes
    },
    'recalculate-health-scores-hourly': {
        'task': 'app.jobs.tasks.recalculate_health_scores',
        'schedule': 3600.0,  # 1 hour
    },
    'check-pm-thresholds-every-6-hours': {
        'task': 'app.jobs.tasks.check_pm_thresholds',
        'schedule': 21600.0,  # 6 hours
    },
    'detect-recurrent-patterns-daily': {
        'task': 'app.jobs.tasks.detect_recurrent_patterns',
        'schedule': crontab(hour=2, minute=0),  # Daily at 2 AM
    },
    'monitor-ot-timers-every-15-minutes': {
        'task': 'app.jobs.tasks.monitor_ot_timers',
        'schedule': 900.0,  # 15 minutes
    },
    'cleanup-old-alerts-weekly': {
        'task': 'app.jobs.tasks.cleanup_old_alerts',
        'schedule': crontab(day_of_week=0, hour=3, minute=0),  # Sunday at 3 AM
    },
}

