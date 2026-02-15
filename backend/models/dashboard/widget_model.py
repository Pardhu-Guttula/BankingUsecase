# Epic Title: Personalized Dashboard

from sqlalchemy import Column, Integer, String, ForeignKey, Boolean
from sqlalchemy.orm import relationship
from backend.app import db

class Widget(db.Model):
    __tablename__ = 'widgets'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    widget_type = Column(String(50), nullable=False)
    is_active = Column(Boolean, default=True, nullable=False)

    user = relationship('User', back_populates='widgets')

    def __init__(self, user_id: int, widget_type: str, is_active: bool = True):
        self.user_id = user_id
        self.widget_type = widget_type
        self.is_active = is_active


# File 2: Widget Repository for CRUD Operations on Widgets in repositories/dashboard/widget_repository.py