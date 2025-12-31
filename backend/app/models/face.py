# Face model
from sqlalchemy import Column, Integer, String, ForeignKey, LargeBinary, DateTime
from sqlalchemy.sql import func
from ..core.database import Base

class Face(Base):
    __tablename__ = "faces"
    
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    encoding = Column(LargeBinary)
    image_path = Column(String)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
