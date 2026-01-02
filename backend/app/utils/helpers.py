from datetime import datetime
from typing import Any, Dict


def format_datetime(dt: datetime) -> str:
    """Format datetime to ISO string"""
    return dt.isoformat()


def safe_dict_get(d: Dict, key: str, default: Any = None) -> Any:
    """Safely get value from dictionary"""
    return d.get(key, default)


def generate_unique_filename(original_filename: str) -> str:
    """Generate unique filename with timestamp"""
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    extension = original_filename[original_filename.rfind('.'):]
    return f"{timestamp}_{original_filename.replace(extension, '')}{extension}"
