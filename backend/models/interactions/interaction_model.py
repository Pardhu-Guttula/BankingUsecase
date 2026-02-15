# Epic Title: Interaction History and Documentation Upload

from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Text
from sqlalchemy.orm import relationship
from backend.app import db
import datetime

class Interaction(db.Model):
    __tablename__ = 'interactions'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    action = Column(String(100), nullable=False)
    details = Column(Text, nullable=True)
    timestamp = Column(DateTime, default=datetime.datetime.utcnow, nullable=False)

    user = relationship("User", back_populates="interactions")

    def __init__(self, user_id: int, action: str, details: str = None):
        self.user_id = user_id
        self.action = action
        self.details = details

        
# File 2: Interaction Repository to Handle CRUD Operations in history/repositories/interaction_repository.py