# Epic Title: Interaction History and Documentation Upload

from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from datetime import datetime
from backend.app import db

class InteractionHistory(db.Model):
    __tablename__ = 'interaction_histories'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    action = Column(String(255), nullable=False)
    timestamp = Column(DateTime, default=datetime.utcnow)

    def __init__(self, user_id: int, action: str):
        self.user_id = user_id
        self.action = action


# File 2: Interaction History Repository for Database Operations in dashboard/repositories/interaction_history_repository.py