# Epic Title: Document Upload Capability

from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from backend.app import db
from datetime import datetime

class Document(db.Model):
    __tablename__ = 'documents'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    filename = Column(String(255), nullable=False)
    filepath = Column(String(500), nullable=False)
    uploaded_at = Column(DateTime, default=datetime.utcnow)

    user = relationship('User', back_populates='documents')

    def __init__(self, user_id: int, filename: str, filepath: str):
        self.user_id = user_id
        self.filename = filename
        self.filepath = filepath
        self.uploaded_at = datetime.utcnow()
        

# File 2: Document Upload Repository in `repositories/documents/document_repository.py`