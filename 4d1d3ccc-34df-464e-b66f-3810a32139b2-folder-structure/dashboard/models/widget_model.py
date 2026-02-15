# Epic Title: Customizable Widgets

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from backend.app import db

class Widget(db.Model):
    __tablename__ = 'widgets'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    name = Column(String(100), nullable=False)
    settings = Column(String(500), nullable=True)

    user = relationship('User', backref='widgets')

    def __init__(self, user_id: int, name: str, settings: str):
        self.user_id = user_id
        self.name = name
        self.settings = settings


# File 2: Widget Repository for Database Operations in dashboard/repositories/widget_repository.py