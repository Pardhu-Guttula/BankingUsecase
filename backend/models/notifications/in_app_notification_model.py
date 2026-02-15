# Epic Title: Real-time Status Updates and Notifications

from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from backend.app import db
import datetime

class InAppNotification(db.Model):
    __tablename__ = 'in_app_notifications'

    id = Column(Integer, primary_key=True)
    request_id = Column(Integer, nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    message = Column(String(255), nullable=False)
    is_read = Column(Boolean, default=False, nullable=False)
    timestamp = Column(DateTime, default=datetime.datetime.utcnow, nullable=False)

    user = relationship('User', back_populates='in_app_notifications')

    def __init__(self, request_id: int, user_id: int, message: str):
        self.request_id = request_id
        self.user_id = user_id
        self.message = message


# File 2: Update User Model to Include Relationship with In-App Notifications in models/authentication/user_model.py