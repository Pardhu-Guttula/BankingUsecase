# Epic Title: Customizable Widgets

from sqlalchemy import Column, Integer, String, ForeignKey
from backend.app import db

class Widget(db.Model):
    __tablename__ = 'widgets'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    widget_type = Column(String(50), nullable=False)
    position = Column(Integer, nullable=False)

    def __init__(self, user_id: int, widget_type: str, position: int):
        self.user_id = user_id
        self.widget_type = widget_type
        self.position = position


# File 2: Widgets Repository in backend/repositories/dashboard/widget_repository.py