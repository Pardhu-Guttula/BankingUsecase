# Epic Title: Interaction History and Documentation Upload

from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from backend.app import db

class Interaction(db.Model):
    __tablename__ = 'interactions'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    action = Column(String(255), nullable=False)
    description = Column(String(255), nullable=True)
    timestamp = Column(DateTime, default=datetime.utcnow)

    user = relationship("User", back_populates="interactions")

    def __init__(self, user_id: int, action: str, description: str = None):
        self.user_id = user_id
        self.action = action
        self.description = description


# File 2: Update User Model to Include Relationship with Interaction in models/authentication/user_model.py