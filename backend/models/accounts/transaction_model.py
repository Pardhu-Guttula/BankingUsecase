# Epic Title: Personalized Dashboard

from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from backend.app import db

class Transaction(db.Model):
    __tablename__ = 'transactions'

    id = Column(Integer, primary_key=True)
    account_id = Column(Integer, ForeignKey('accounts.id'), nullable=False)
    amount = Column(Float, nullable=False)
    transaction_type = Column(String(20), nullable=False)
    description = Column(String(255), nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)

    account = relationship("Account", back_populates="transactions")

    def __init__(self, account_id: int, amount: float, transaction_type: str, description: str = None):
        self.account_id = account_id
        self.amount = amount
        self.transaction_type = transaction_type
        self.description = description


# File 3: Update User Model to Include Relationship with Account in models/authentication/user_model.py