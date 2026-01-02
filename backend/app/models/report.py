from sqlalchemy import Column, Integer, String, DateTime, Text
from datetime import datetime
from app.core.database import Base


class Report(Base):
    __tablename__ = "reports"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    report_type = Column(String, nullable=False)  # 'daily', 'weekly', 'monthly'
    content = Column(Text, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)
