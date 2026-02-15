# Epic Title: Interaction History and Documentation Upload

from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Text
from sqlalchemy.orm import relationship
from datetime import datetime
from backend.app import db

class Application(db.Model):
    __tablename__ = 'applications'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    status = Column(String(50), nullable=False)
    data = Column(Text, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, onupdate=datetime.utcnow)

    user = relationship("User", back_populates="applications")

    def __init__(self, user_id: int, status: str, data: str = None):
        self.user_id = user_id
        self.status = status
        self.data = data


# File 2: Update User Model to Include Relationship with Application in models/authentication/user_model.py