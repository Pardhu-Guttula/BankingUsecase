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
    external_id = Column(String(100), unique=True, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)

    def __init__(self, user_id: int, amount: float, status: str = 'pending', external_id: str):
        self.user_id = user_id
        self.amount = amount
        self.status = status
        self.external_id = external_id

# File 4: Update Request Model to Include External ID in models/core_banking/request_model.py (Modified)