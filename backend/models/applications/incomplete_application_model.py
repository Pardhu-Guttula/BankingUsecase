# Epic Title: Save and Resume Incomplete Applications

from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from backend.app import db
from datetime import datetime

class IncompleteApplication(db.Model):
    __tablename__ = 'incomplete_applications'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    application_data = Column(Text, nullable=False)
    saved_at = Column(DateTime, default=datetime.utcnow)

    user = relationship('User', back_populates='incomplete_applications')

    def __init__(self, user_id: int, application_data: str):
        self.user_id = user_id
        self.application_data = application_data
        self.saved_at = datetime.utcnow()


# File 2: Incomplete Application Repository in `repositories/applications/incomplete_application_repository.py`