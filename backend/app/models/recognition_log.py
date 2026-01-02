# Recognition log model
from sqlalchemy import Column, Integer, String, ForeignKey, Boolean, Float, DateTime
from sqlalchemy.sql import func
from ..core.database import Base

class RecognitionLog(Base):
    __tablename__ = "recognition_logs"
    
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    action = Column(String)  # "enroll", "verify"
    success = Column(Boolean)
    confidence = Column(Float)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
