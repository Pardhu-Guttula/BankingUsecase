# Epic Title: Real-time Status Updates and Notifications

from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from backend.app import db
import datetime

class Notification(db.Model):
    __tablename__ = 'notifications'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    message = Column(String(255), nullable=False)
    is_read = Column(Boolean, default=False, nullable=False)
    created_at = Column(DateTime, default=datetime.datetime.utcnow, nullable=False)

    user = relationship("User", back_populates="notifications")

    def __init__(self, user_id: int, message: str):
        self.user_id = user_id
        self.message = message
        self.created_at = datetime.datetime.utcnow()

        
# File 2: Notification Repository to Handle CRUD Operations in notifications/repositories/notification_repository.py