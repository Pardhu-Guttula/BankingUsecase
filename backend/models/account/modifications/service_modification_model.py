# Epic Title: Account Opening and Service Modifications

from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from backend.app import db

class ServiceModificationRequest(db.Model):
    __tablename__ = 'service_modification_requests'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    service_type = Column(String(50), nullable=False)
    modification_details = Column(String(255), nullable=False)
    status = Column(String(20), default='pending', nullable=False)
    submitted_at = Column(DateTime, default=datetime.utcnow, nullable=False)

    user = relationship('User', back_populates='service_modifications')

    def __init__(self, user_id: int, service_type: str, modification_details: str, status: str = 'pending', submitted_at: DateTime = None):
        self.user_id = user_id
        self.service_type = service_type
        self.modification_details = modification_details
        self.status = status
        if submitted_at is None:
            submitted_at = datetime.utcnow()
        self.submitted_at = submitted_at


# File 2: Service Modification Request Repository in repositories/account/modifications/service_modification_repository.py