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
    created_at = Column(DateTime, default=datetime.utcnow)

    def __init__(self, user_id: int, type: str, status: str = 'pending'):
        self.user_id = user_id
        self.type = type
        self.status = status

# File 6: Transaction Repository in repositories/core_banking/transaction_repository.py