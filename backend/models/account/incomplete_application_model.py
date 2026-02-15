# Epic Title: Interaction History and Documentation Upload

from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from backend.app import db

class IncompleteApplication(db.Model):
    __tablename__ = 'incomplete_applications'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, nullable=False)
    status = Column(String(50), nullable=False)
    application_data = Column(Text, nullable=False)
    saved_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    
    def __init__(self, user_id: int, status: str, application_data: str):
        self.user_id = user_id
        self.status = status
        self.application_data = application_data

# File 2: IncompleteApplication Repository in repositories/account/incomplete_application_repository.py