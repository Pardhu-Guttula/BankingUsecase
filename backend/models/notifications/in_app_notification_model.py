# Epic Title: Real-time Status Updates and Notifications

from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from backend.app import db


class InAppNotification(db.Model):
    __tablename__ = 'in_app_notifications'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    message = Column(String, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)

    user = relationship('User', back_populates='in_app_notifications')

    def __init__(self, user_id: int, message: str, created_at: DateTime = None):
        self.user_id = user_id
        self.message = message
        if created_at is None:
            created_at = datetime.utcnow()
        self.created_at = created_at


# File 2: In-App Notification Repository for Data Access in repositories/notifications/in_app_notification_repository.py