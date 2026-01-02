from pydantic import BaseModel
from datetime import datetime
from typing import Optional


class FaceBase(BaseModel):
    user_id: int


class FaceCreate(FaceBase):
    encoding: bytes


class FaceInDB(FaceBase):
    id: int
    image_path: Optional[str]
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True


class Face(FaceInDB):
    pass


class FaceEnrollRequest(BaseModel):
    user_id: int


class FaceVerifyResponse(BaseModel):
    success: bool
    user_id: Optional[int] = None
    confidence: Optional[float] = None
    message: str
