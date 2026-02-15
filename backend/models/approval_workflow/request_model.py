# Epic Title: Account Opening and Service Modifications

from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from backend.app import db
import datetime

class Request(db.Model):
    __tablename__ = 'requests'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    request_type = Column(String(50), nullable=False)
    description = Column(String(255), nullable=True)
    status = Column(String(20), default='Pending', nullable=False)
    created_at = Column(DateTime, default=datetime.datetime.utcnow, nullable=False)
    updated_at = Column(DateTime, default=datetime.datetime.utcnow, nullable=False)

    user = relationship("User")

    def __init__(self, user_id: int, request_type: str, description: str, status: str = 'Pending'):
        self.user_id = user_id
        self.request_type = request_type
        self.description = description
        self.status = status


# File 2: Request Repository to Handle CRUD Operations for Requests in approval_workflow/repositories/request_repository.py