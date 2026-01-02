# Helper functions
from datetime import datetime

def format_datetime(dt):
    """Format datetime to string"""
    return dt.strftime("%Y-%m-%d %H:%M:%S")

def truncate_text(text, length=50):
    """Truncate text to specified length"""
    return text[:length] + "..." if len(text) > length else text
