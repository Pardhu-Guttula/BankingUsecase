# Epic Title: Interaction History and Documentation Upload

from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from backend.app import db
from datetime import datetime

class Document(db.Model):
    __tablename__ = 'documents'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    filename = Column(String(255), nullable=False)
    file_path = Column(String(255), nullable=False)
    uploaded_at = Column(DateTime, nullable=False, default=datetime.utcnow)

    def __init__(self, user_id: int, filename: str, file_path: str, uploaded_at: datetime = datetime.utcnow()):
        self.user_id = user_id
        self.filename = filename
        self.file_path = file_path
        self.uploaded_at = uploaded_at

# File 2: Document Repository in repositories/documents/document_repository.py