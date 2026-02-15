# Epic Title: Core Banking System Integration

from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from datetime import datetime
from backend.app import db

class Request(db.Model):
    __tablename__ = 'requests'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    type = Column(String(50), nullable=False)
    status = Column(String(50), nullable=False, default='pending')
    external_id = Column(String(100), unique=True, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)

    def __init__(self, user_id: int, type: str, status: str = 'pending', external_id: str):
        self.user_id = user_id
        self.type = type
        self.status = status
        self.external_id = external_id

# File 5: Update Transaction Repository to Include External ID Handling in repositories/core_banking/transaction_repository.py (Modified)