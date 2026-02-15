# Epic Title: Real-time Status Updates

from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from backend.app import db
from datetime import datetime

class RequestStatus(db.Model):
    __tablename__ = 'request_statuses'

    id = Column(Integer, primary_key=True)
    request_id = Column(Integer, nullable=False)
    status = Column(String(50), nullable=False)
    updated_at = Column(DateTime, default=datetime.utcnow)
    request_type = Column(String(50), nullable=False)

    def __init__(self, request_id: int, status: str, request_type: str):
        self.request_id = request_id
        self.status = status
        self.updated_at = datetime.utcnow()
        self.request_type = request_type


# File 2: Status Update Repository in repositories/status/request_status_repository.py