# Epic Title: Real-time Status Updates and Notifications

from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from backend.app import db


class EmailNotification(db.Model):
    __tablename__ = 'email_notifications'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    subject = Column(String(255), nullable=False)
    content = Column(String, nullable=False)
    sent_at = Column(DateTime, default=datetime.utcnow, nullable=False)

    user = relationship('User', back_populates='email_notifications')

    def __init__(self, user_id: int, subject: String, content: String, sent_at: DateTime = None):
        self.user_id = user_id
        self.subject = subject
        self.content = content
        if sent_at is None:
            sent_at = datetime.utcnow()
        self.sent_at = sent_at


# File 2: Notification Repository for Data Access in repositories/notifications/email_notification_repository.py