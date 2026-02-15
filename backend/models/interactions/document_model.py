# Epic Title: Interaction History and Documentation Upload

from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from backend.app import db
from datetime import datetime

class Document(db.Model):
    __tablename__ = 'documents'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    request_id = Column(Integer, nullable=False)
    file_name = Column(String(255), nullable=False)
    file_path = Column(String(255), nullable=False)
    uploaded_at = Column(DateTime, default=datetime.utcnow)

    user = db.relationship("User", back_populates="documents")

    def __init__(self, user_id: int, request_id: int, file_name: str, file_path: str):
        self.user_id = user_id
        self.request_id = request_id
        self.file_name = file_name
        self.file_path = file_path


# File 2: Update User Model to Include Relationship with Document in models/authentication/user_model.py