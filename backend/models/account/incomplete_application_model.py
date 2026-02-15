# Epic Title: Interaction History and Documentation Upload

from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from backend.app import db
from datetime import datetime

class IncompleteApplication(db.Model):
    __tablename__ = 'incomplete_applications'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    form_data = Column(Text, nullable=False)
    saved_at = Column(DateTime, nullable=False, default=datetime.utcnow)

    user = relationship("User", back_populates="incomplete_applications")

    def __init__(self, user_id: int, form_data: str, saved_at: datetime = datetime.utcnow()):
        self.user_id = user_id
        self.form_data = form_data
        self.saved_at = saved_at

# File 2: Incomplete Application Repository in repositories/account/incomplete_application_repository.py