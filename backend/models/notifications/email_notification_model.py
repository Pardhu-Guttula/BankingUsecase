# Epic Title: Real-time Status Updates and Notifications

from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Boolean
from sqlalchemy.orm import relationship
from backend.app import db
import datetime

class EmailNotification(db.Model):
    __tablename__ = 'email_notifications'

    id = Column(Integer, primary_key=True)
    request_id = Column(Integer, nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    email = Column(String(100), nullable=False)
    subject = Column(String(255), nullable=False)
    content = Column(String(255), nullable=False)
    sent = Column(Boolean, default=False, nullable=False)
    timestamp = Column(DateTime, default=datetime.datetime.utcnow, nullable=False)

    user = relationship('User', back_populates='email_notifications')

    def __init__(self, request_id: int, user_id: int, email: str, subject: str, content: str):
        self.request_id = request_id
        self.user_id = user_id
        self.email = email
        self.subject = subject
        self.content = content


# File 2: Update User Model to Include Relationship with Email Notifications in models/authentication/user_model.py