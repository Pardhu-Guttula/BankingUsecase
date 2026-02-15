# Epic Title: Interaction History and Documentation Upload

from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Text
from datetime import datetime
from backend.app import db


class IncompleteApplication(db.Model):
    __tablename__ = 'incomplete_applications'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    application_data = Column(Text, nullable=False)
    saved_at = Column(DateTime, default=datetime.utcnow, nullable=False)

    def __init__(self, user_id: int, application_data: str, saved_at: DateTime = None):
        self.user_id = user_id
        self.application_data = application_data
        if saved_at is None:
            saved_at = datetime.utcnow()
        self.saved_at = saved_at


# File 2: Incomplete Application Repository for Data Access in repositories/account/incomplete_application_repository.py