# Epic Title: Account Opening and Service Modifications

from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from backend.app import db
from datetime import datetime

class ServiceModification(db.Model):
    __tablename__ = 'service_modifications'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    service_type = Column(String(50), nullable=False)
    status = Column(String(50), nullable=False, default='Pending')
    submitted_at = Column(DateTime, nullable=False, default=datetime.utcnow)

    user = relationship('User', backref='service_modifications')

    def __init__(self, user_id: int, service_type: str, status: str = 'Pending'):
        self.user_id = user_id
        self.service_type = service_type
        self.status = status

# File 2: Service Modification Repository in repositories/account/modifications/service_modification_repository.py