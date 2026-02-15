# Epic Title: Real-time Status Updates and Notifications

from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from backend.app import db
import datetime

class Status(db.Model):
    __tablename__ = 'statuses'

    id = Column(Integer, primary_key=True)
    request_id = Column(Integer, ForeignKey('requests.id'), nullable=False)
    status = Column(String(50), nullable=False)
    updated_at = Column(DateTime, default=datetime.datetime.utcnow, nullable=False)

    request = relationship("Request", back_populates="statuses")

    def __init__(self, request_id: int, status: str):
        self.request_id = request_id
        self.status = status
        self.updated_at = datetime.datetime.utcnow()


# File 2: Status Repository to Manage Status CRUD Operations in status/repositories/status_repository.py