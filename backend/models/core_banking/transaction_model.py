# Epic Title: Core Banking System Integration

from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey
from datetime import datetime
from backend.app import db

class Transaction(db.Model):
    __tablename__ = 'transactions'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    amount = Column(Float, nullable=False)
    status = Column(String(50), nullable=False, default='pending')
    created_at = Column(DateTime, default=datetime.utcnow)

    def __init__(self, user_id: int, amount: float, status: str = 'pending'):
        self.user_id = user_id
        self.amount = amount
        self.status = status

# File 5: Request Model in models/core_banking/request_model.py