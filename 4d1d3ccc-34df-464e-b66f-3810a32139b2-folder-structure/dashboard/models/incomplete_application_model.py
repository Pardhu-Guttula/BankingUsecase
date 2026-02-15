# Epic Title: Interaction History and Documentation Upload

from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey
from datetime import datetime
from backend.app import db

class IncompleteApplication(db.Model):
    __tablename__ = 'incomplete_applications'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    application_data = Column(Text, nullable=False)
    saved_at = Column(DateTime, default=datetime.utcnow)

    def __init__(self, user_id: int, application_data: str):
        self.user_id = user_id
        self.application_data = application_data


# File 2: Incomplete Application Repository for Database Operations in dashboard/repositories/incomplete_application_repository.py