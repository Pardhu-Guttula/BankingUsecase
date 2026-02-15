# Epic Title: Real-time Status Updates and Notifications

from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from backend.app import db
from datetime import datetime

class InAppNotification(db.Model):
    __tablename__ = 'in_app_notifications'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    message = Column(String(255), nullable=False)
    timestamp = Column(DateTime, nullable=False, default=datetime.utcnow)
    seen = Column(Integer, nullable=False, default=0)

    def __init__(self, user_id: int, message: str, timestamp: datetime = datetime.utcnow(), seen: int = 0):
        self.user_id = user_id
        self.message = message
        self.timestamp = timestamp
        self.seen = seen

# File 2: In-App Notification Repository in repositories/notifications/in_app_notification_repository.py