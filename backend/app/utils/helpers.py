# Helper functions
from datetime import datetime
from typing import Any

def format_datetime(dt: datetime) -> str:
    """Format datetime to string"""
    return dt.strftime("%Y-%m-%d %H:%M:%S")

def safe_get(dictionary: dict, key: str, default: Any = None):
    """Safely get value from dictionary"""
    return dictionary.get(key, default)
