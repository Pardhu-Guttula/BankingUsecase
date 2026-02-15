# Epic Title: In-app Notifications

from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from backend.app import db
from datetime import datetime

class InAppNotification(db.Model):
    __tablename__ = 'in_app_notifications'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    message = Column(String(500), nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    seen = Column(Integer, default=0)  # 0 indicates not seen, 1 indicates seen
    user = relationship('User', back_populates='in_app_notifications')

    def __init__(self, user_id: int, message: str):
        self.user_id = user_id
        self.message = message
        self.created_at = datetime.utcnow()


# File 2: In-App Notification Repository in `repositories/notifications/in_app_notification_repository.py`