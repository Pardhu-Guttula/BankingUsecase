# Epic Title: Real-time Status Updates and Notifications

from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from backend.app import db
from datetime import datetime

class RequestStatus(db.Model):
    __tablename__ = 'request_statuses'

    id = Column(Integer, primary_key=True)
    request_id = Column(Integer, nullable=False)
    status = Column(String(50), nullable=False)
    last_updated = Column(DateTime, nullable=False, default=datetime.utcnow)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)

    def __init__(self, request_id: int, status: str, user_id: int, last_updated: datetime = datetime.utcnow()):
        self.request_id = request_id
        self.status = status
        self.user_id = user_id
        self.last_updated = last_updated

# File 2: Request Status Repository in repositories/status/request_status_repository.py