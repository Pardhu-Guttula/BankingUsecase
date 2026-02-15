# Epic Title: Personalized Dashboard

from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from datetime import datetime
from backend.app import db


class Widget(db.Model):
    __tablename__ = 'widgets'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    widget_type = Column(String(255), nullable=False)
    position = Column(Integer, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)

    def __init__(self, user_id: int, widget_type: str, position: int, created_at: DateTime = None):
        self.user_id = user_id
        self.widget_type = widget_type
        self.position = position
        if created_at is None:
            created_at = datetime.utcnow()
        self.created_at = created_at


# File 2: Widget Repository in repositories/dashboard/widget_repository.py