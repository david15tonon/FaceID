# Face schemas
from pydantic import BaseModel
from datetime import datetime

class FaceBase(BaseModel):
    user_id: int

class FaceCreate(FaceBase):
    image_data: str

class FaceResponse(FaceBase):
    id: int
    image_path: str
    created_at: datetime
    
    class Config:
        from_attributes = True
