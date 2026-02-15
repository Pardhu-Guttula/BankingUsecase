# Epic Title: Real-time Status Updates and Notifications

from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from datetime import datetime
from backend.app import db

class StatusUpdate(db.Model):
    __tablename__ = 'status_updates'

    id = Column(Integer, primary_key=True)
    request_id = Column(Integer, ForeignKey('service_modification_requests.id'), nullable=False)
    status = Column(String(50), nullable=False)
    updated_at = Column(DateTime, default=datetime.utcnow)

    request = db.relationship('ServiceModificationRequest', backref='status_updates')

    def __init__(self, request_id: int, status: str):
        self.request_id = request_id
        self.status = status


# File 2: Status Update Repository for Database Operations in dashboard/repositories/status_update_repository.py