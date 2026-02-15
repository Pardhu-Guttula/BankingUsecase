# Epic Title: Maintain Interaction History

from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from backend.app import db
from datetime import datetime

class Interaction(db.Model):
    __tablename__ = 'interactions'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    action = Column(String(255), nullable=False)
    timestamp = Column(DateTime, default=datetime.utcnow)

    user = relationship('User', back_populates='interactions')

    def __init__(self, user_id: int, action: str):
        self.user_id = user_id
        self.action = action
        self.timestamp = datetime.utcnow()


# File 2: Interaction History Repository in `repositories/history/interaction_repository.py`