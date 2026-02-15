# Epic Title: Interaction History and Documentation Upload

from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Text
from sqlalchemy.orm import relationship
from backend.app import db
import datetime

class IncompleteApplication(db.Model):
    __tablename__ = 'incomplete_applications'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    data = Column(Text, nullable=False)
    last_updated = Column(DateTime, default=datetime.datetime.utcnow, nullable=False)

    user = relationship('User', back_populates='incomplete_applications')

    def __init__(self, user_id: int, data: str):
        self.user_id = user_id
        self.data = data


# File 2: Update User Model to Include Relationship with Incomplete Applications in models/authentication/user_model.py