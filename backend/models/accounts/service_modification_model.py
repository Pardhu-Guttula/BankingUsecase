# Epic Title: Account Opening and Service Modifications

from sqlalchemy import Column, Integer, String, ForeignKey, Text
from backend.app import db

class ServiceModification(db.Model):
    __tablename__ = 'service_modifications'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    service_type = Column(String(20), nullable=False)
    description = Column(Text, nullable=False)
    status = Column(String(20), default='Pending', nullable=False)

    def __init__(self, user_id: int, service_type: str, description: str, status: str = 'Pending'):
        self.user_id = user_id
        self.service_type = service_type
        self.description = description
        self.status = status

# File 5: Service Modification Repository to Save Modification Requests in account/repositories/service_modification_repository.py