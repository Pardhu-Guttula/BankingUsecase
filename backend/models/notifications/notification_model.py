# Epic Title: Real-time Status Updates and Notifications

from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from backend.app import db

class Notification(db.Model):
    __tablename__ = 'notifications'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, nullable=False)
    request_id = Column(Integer, ForeignKey('requests.id'), nullable=False)
    message = Column(String(255), nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    
    def __init__(self, user_id: int, request_id: int, message: str):
        self.user_id = user_id
        self.request_id = request_id
        self.message = message

# File 4: Register In-App Notification Blueprint in app.py (Already Exists, Modified)