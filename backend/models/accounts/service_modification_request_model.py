# Epic Title: Account Opening and Service Modifications

from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from backend.app import db

class ServiceModificationRequest(db.Model):
    __tablename__ = 'service_modification_requests'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    service_name = Column(String(50), nullable=False)
    modification_details = Column(String(255), nullable=False)
    status = Column(String(20), nullable=False, default='pending')
    created_at = Column(DateTime, default=datetime.utcnow)

    user = relationship("User", back_populates="service_modification_requests")

    def __init__(self, user_id: int, service_name: str, modification_details: str, status: str = 'pending'):
        self.user_id = user_id
        self.service_name = service_name
        self.modification_details = modification_details
        self.status = status


# File 2: Update User Model to Include Relationship with ServiceModificationRequest in models/authentication/user_model.py