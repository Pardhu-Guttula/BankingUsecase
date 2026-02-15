# Epic Title: Interaction History and Documentation Upload

from sqlalchemy import Column, Integer, String, LargeBinary, DateTime, ForeignKey
from datetime import datetime
from backend.app import db

class Document(db.Model):
    __tablename__ = 'documents'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    request_id = Column(Integer, ForeignKey('service_modification_requests.id'), nullable=False)
    filename = Column(String(255), nullable=False)
    file_data = Column(LargeBinary, nullable=False)
    uploaded_at = Column(DateTime, default=datetime.utcnow)

    def __init__(self, user_id: int, request_id: int, filename: str, file_data: bytes):
        self.user_id = user_id
        self.request_id = request_id
        self.filename = filename
        self.file_data = file_data


# File 2: Document Repository for Database Operations in dashboard/repositories/document_repository.py