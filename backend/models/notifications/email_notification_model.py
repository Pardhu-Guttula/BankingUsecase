# Epic Title: Email Notifications

from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from backend.app import db
from datetime import datetime

class EmailNotification(db.Model):
    __tablename__ = 'email_notifications'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    subject = Column(String(255), nullable=False)
    body = Column(String(2000), nullable=False)
    sent_at = Column(DateTime, default=datetime.utcnow)
    user = relationship('User', back_populates='email_notifications')

    def __init__(self, user_id: int, subject: str, body: str):
        self.user_id = user_id
        self.subject = subject
        self.body = body
        self.sent_at = datetime.utcnow()


# File 2: Email Notification Repository in `repositories/notifications/email_notification_repository.py`