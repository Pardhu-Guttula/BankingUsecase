# Epic Title: Interaction History and Documentation Upload

from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from backend.app import db
from datetime import datetime

class InteractionHistory(db.Model):
    __tablename__ = 'interaction_histories'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    action = Column(String(255), nullable=False)
    timestamp = Column(DateTime, nullable=False, default=datetime.utcnow)

    def __init__(self, user_id: int, action: str, timestamp: datetime = datetime.utcnow()):
        self.user_id = user_id
        self.action = action
        self.timestamp = timestamp

# File 2: Interaction History Repository in repositories/interactions/interaction_history_repository.py