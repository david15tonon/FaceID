import hashlib
import base64


def hash_string(text: str) -> str:
    """Hash a string using SHA256"""
    return hashlib.sha256(text.encode()).hexdigest()


def encode_base64(data: bytes) -> str:
    """Encode bytes to base64 string"""
    return base64.b64encode(data).decode('utf-8')


def decode_base64(text: str) -> bytes:
    """Decode base64 string to bytes"""
    return base64.b64decode(text.encode('utf-8'))


def sanitize_filename(filename: str) -> str:
    """Sanitize filename for safe storage"""
    # Remove or replace unsafe characters
    unsafe_chars = ['/', '\\', '..', '<', '>', ':', '"', '|', '?', '*']
    safe_name = filename
    for char in unsafe_chars:
        safe_name = safe_name.replace(char, '_')
    return safe_name
