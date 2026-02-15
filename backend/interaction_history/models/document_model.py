# Epic Title: Document Upload Capability

from datetime import datetime
from backend.app import db

class Document(db.Model):
    __tablename__ = 'documents'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, nullable=False)
    filename = db.Column(db.String(256), nullable=False)
    upload_time = db.Column(db.DateTime, default=datetime.utcnow)

    def __init__(self, user_id: int, filename: str):
        self.user_id = user_id
        self.filename = filename


# File 2: Document Repository for Database Operations in interaction_history/repositories/document_repository.py