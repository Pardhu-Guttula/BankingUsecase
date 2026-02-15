# Epic Title: Account Opening and Service Modifications

from sqlalchemy import Column, Integer, String, Text, ForeignKey
from datetime import datetime
from backend.app import db

class ServiceModificationRequest(db.Model):
    __tablename__ = 'service_modification_requests'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    service_name = Column(String(100), nullable=False)
    modification_type = Column(String(10), nullable=False)
    reason = Column(Text, nullable=False)
    status = Column(String(20), default='pending', nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)

    def __init__(self, user_id: int, service_name: str, modification_type: str, reason: str, status: str = 'pending'):
        self.user_id = user_id
        self.service_name = service_name
        self.modification_type = modification_type
        self.reason = reason
        self.status = status


# File 6: Service Modification Template to Provide User Interface in templates/modify_service.html