# Epic Title: Personalized Dashboard

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from backend.app import db

class Widget(db.Model):
    __tablename__ = 'widgets'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    name = Column(String(50), nullable=False)
    position = Column(Integer, nullable=False)

    user = relationship('User', backref='widgets')

    def __init__(self, user_id: int, name: str, position: int):
        self.user_id = user_id
        self.name = name
        self.position = position

# File 2: Widget Repository for Managing Widgets in repositories/dashboard/widget_repository.py