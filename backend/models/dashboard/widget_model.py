# Epic Title: Personalized Dashboard

from sqlalchemy import Column, Integer, String, ForeignKey
from backend.app import db

class Widget(db.Model):
    __tablename__ = 'widgets'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    name = Column(String(50), nullable=False)
    config = Column(String(255), nullable=False)

    def __init__(self, user_id: int, name: str, config: str):
        self.user_id = user_id
        self.name = name
        self.config = config


# File 2: Widget Repository to Manage Widgets in dashboard/repositories/widget_repository.py