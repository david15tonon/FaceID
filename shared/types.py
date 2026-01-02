from enum import Enum
from typing import Optional, List
from dataclasses import dataclass


class UserRole(Enum):
    """User roles"""
    ADMIN = "admin"
    USER = "user"
    GUEST = "guest"


class RecognitionStatus(Enum):
    """Recognition status"""
    SUCCESS = "success"
    FAILED = "failed"
    PENDING = "pending"


@dataclass
class FaceData:
    """Face data structure"""
    id: int
    user_id: int
    encoding: bytes
    image_path: Optional[str] = None
    created_at: Optional[str] = None


@dataclass
class UserData:
    """User data structure"""
    id: int
    email: str
    name: str
    is_active: bool = True
    role: UserRole = UserRole.USER
