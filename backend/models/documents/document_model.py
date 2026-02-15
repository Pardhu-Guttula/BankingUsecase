# Epic Title: Interaction History and Documentation Upload

from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from backend.app import db
import datetime

class Document(db.Model):
    __tablename__ = 'documents'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    filename = Column(String(255), nullable=False)
    path = Column(String(255), unique=True, nullable=False)
    uploaded_at = Column(DateTime, default=datetime.datetime.utcnow, nullable=False)

    user = relationship('User', back_populates='documents')

    def __init__(self, user_id: int, filename: str, path: str):
        self.user_id = user_id
        self.filename = filename
        self.path = path


# File 2: Update User Model to Include Relationship with Documents in models/authentication/user_model.py