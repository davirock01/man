from datetime import datetime, timedelta
from typing import Optional
import uuid


def generate_uuid() -> str:
    """Generate a UUID string."""
    return str(uuid.uuid4())


def calculate_percentage(current: float, total: float) -> float:
    """Calculate percentage, handling division by zero."""
    if total == 0:
        return 0.0
    return (current / total) * 100


def days_between(date1: datetime, date2: datetime) -> int:
    """Calculate days between two dates."""
    return abs((date2 - date1).days)


def add_days(date: datetime, days: int) -> datetime:
    """Add days to a date."""
    return date + timedelta(days=days)


def format_datetime(dt: datetime) -> str:
    """Format datetime to ISO string."""
    return dt.isoformat()


def truncate_string(text: str, max_length: int = 100) -> str:
    """Truncate string to max length."""
    if len(text) <= max_length:
        return text
    return text[:max_length - 3] + "..."


