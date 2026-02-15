# Epic Title: Real-time Status Updates and Notifications

from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from backend.app import db

class StatusUpdate(db.Model):
    __tablename__ = 'status_updates'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    request_id = Column(Integer, nullable=False)
    update_message = Column(String(255), nullable=False)
    status = Column(String(20), nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)

    user = relationship("User", back_populates="status_updates")

    def __init__(self, user_id: int, request_id: int, update_message: str, status: str):
        self.user_id = user_id
        self.request_id = request_id
        self.update_message = update_message
        self.status = status


# File 2: Update User Model to Include Relationship with StatusUpdate in models/authentication/user_model.py