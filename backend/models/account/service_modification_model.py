# Epic Title: Account Opening and Service Modifications

from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from backend.app import db
import datetime

class ServiceModification(db.Model):
    __tablename__ = 'service_modifications'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    service_name = Column(String(100), nullable=False)
    action = Column(String(50), nullable=False)
    status = Column(String(20), default='Pending', nullable=False)
    request_date = Column(DateTime, default=datetime.datetime.utcnow, nullable=False)
    approval_date = Column(DateTime)

    user = relationship('User', back_populates='service_modifications')

    def __init__(self, user_id: int, service_name: str, action: str, status: str = 'Pending', approval_date: datetime.datetime = None):
        self.user_id = user_id
        self.service_name = service_name
        self.action = action
        self.status = status
        self.approval_date = approval_date


# File 3: Update User Model to Include Relationship with Service Modifications in models/authentication/user_model.py