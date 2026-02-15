# Epic Title: Personalized Dashboard

from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from backend.app import db

class Widget(db.Model):
    __tablename__ = 'widgets'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    widget_name = Column(String(50), nullable=False)
    widget_settings = Column(String(255), nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)

    user = relationship("User", back_populates="widgets")

    def __init__(self, user_id: int, widget_name: str, widget_settings: str = None):
        self.user_id = user_id
        self.widget_name = widget_name
        self.widget_settings = widget_settings


# File 2: Update User Model to Include Relationship with Widget in models/authentication/user_model.py