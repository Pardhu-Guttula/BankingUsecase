# Epic Title: Real-time Status Updates and Notifications

from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from backend.app import db
import datetime

class RequestStatus(db.Model):
    __tablename__ = 'request_statuses'

    id = Column(Integer, primary_key=True)
    request_id = Column(Integer, nullable=False)
    status = Column(String(50), nullable=False)
    timestamp = Column(DateTime, default=datetime.datetime.utcnow, nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)

    user = relationship('User', back_populates='statuses')

    def __init__(self, request_id: int, status: str, user_id: int):
        self.request_id = request_id
        self.status = status
        self.user_id = user_id


# File 2: Update User Model to Include Relationship with Statuses in models/authentication/user_model.py