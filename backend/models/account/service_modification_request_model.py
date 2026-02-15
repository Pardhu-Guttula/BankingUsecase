# Epic Title: Account Opening and Service Modifications

from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from datetime import datetime
from backend.app import db

class ServiceModificationRequest(db.Model):
    __tablename__ = 'service_modification_requests'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    service_type = Column(String(100), nullable=False)
    status = Column(String(50), nullable=False, default="pending")
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)

    def __init__(self, user_id: int, service_type: str, status: str = "pending"):
        self.user_id = user_id
        self.service_type = service_type
        self.status = status

# File 2: Service Modification Request Repository in repositories/account/service_modification_request_repository.py