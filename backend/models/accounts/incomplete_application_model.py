# Epic Title: Interaction History and Documentation Upload

from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Text
from sqlalchemy.orm import relationship
from backend.app import db
import datetime

class IncompleteApplication(db.Model):
    __tablename__ = 'incomplete_applications'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    application_data = Column(Text, nullable=False)
    saved_at = Column(DateTime, default=datetime.datetime.utcnow, nullable=False)

    user = relationship("User", back_populates="incomplete_applications")

    def __init__(self, user_id: int, application_data: str):
        self.user_id = user_id
        self.application_data = application_data


# File 2: Incomplete Application Repository to Handle CRUD Operations in account/repositories/incomplete_application_repository.py