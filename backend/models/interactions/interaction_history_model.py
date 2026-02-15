# Epic Title: Interaction History and Documentation Upload

from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from backend.app import db
import datetime

class InteractionHistory(db.Model):
    __tablename__ = 'interaction_histories'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    action = Column(String(255), nullable=False)
    timestamp = Column(DateTime, default=datetime.datetime.utcnow, nullable=False)

    user = relationship('User', back_populates='interactions')

    def __init__(self, user_id: int, action: str):
        self.user_id = user_id
        self.action = action


# File 2: Update User Model to Include Relationship with Interaction History in models/authentication/user_model.py