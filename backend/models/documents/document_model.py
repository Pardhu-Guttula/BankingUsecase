# Epic Title: Interaction History and Documentation Upload

from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from backend.app import db
import datetime

class Document(db.Model):
    __tablename__ = 'documents'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    filename = Column(String(255), nullable=False)
    filepath = Column(String(255), nullable=False)
    upload_timestamp = Column(DateTime, default=datetime.datetime.utcnow, nullable=False)

    def __init__(self, user_id: int, filename: str, filepath: str):
        self.user_id = user_id
        self.filename = filename
        self.filepath = filepath


# File 2: Document Repository to Handle CRUD Operations in documents/repositories/document_repository.py