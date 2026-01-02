from datetime import datetime
from typing import Any


def format_timestamp(timestamp: str) -> str:
    """Format timestamp to readable string"""
    try:
        dt = datetime.fromisoformat(timestamp)
        return dt.strftime("%Y-%m-%d %H:%M:%S")
    except:
        return timestamp


def format_confidence(confidence: float) -> str:
    """Format confidence score as percentage"""
    return f"{confidence * 100:.1f}%"


def truncate_text(text: str, max_length: int = 50) -> str:
    """Truncate text to maximum length"""
    if len(text) <= max_length:
        return text
    return text[:max_length-3] + "..."


def generate_unique_id() -> str:
    """Generate unique ID"""
    import uuid
    return str(uuid.uuid4())
