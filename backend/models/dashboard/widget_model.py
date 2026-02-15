# Epic Title: Personalized Dashboard

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from backend.app import db

class Widget(db.Model):
    __tablename__ = 'widgets'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    widget_type = Column(String(50), nullable=False)
    widget_data = Column(String(255), nullable=True)

    user = relationship('User', back_populates='widgets')

    def __init__(self, user_id: int, widget_type: str, widget_data: str = None):
        self.user_id = user_id
        self.widget_type = widget_type
        self.widget_data = widget_data


# File 2: Update User Model to Include Relationship with Widgets in models/authentication/user_model.py