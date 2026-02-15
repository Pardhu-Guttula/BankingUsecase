# Epic Title: Personalized Dashboard

from sqlalchemy import Column, Integer, String, ForeignKey
from backend.app import db

class Widget(db.Model):
    __tablename__ = 'widgets'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    widget_type = Column(String(50), nullable=False)

    def __init__(self, user_id: int, widget_type: str):
        self.user_id = user_id
        self.widget_type = widget_type

# File 2: Widget Repository in repositories/dashboard/widget_repository.py