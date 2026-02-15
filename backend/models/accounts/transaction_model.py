# Epic Title: Personalized Dashboard

from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Numeric
from sqlalchemy.orm import relationship
from datetime import datetime
from backend.app import db

class Transaction(db.Model):
    __tablename__ = 'transactions'

    id = Column(Integer, primary_key=True)
    account_id = Column(Integer, ForeignKey('accounts.id'), nullable=False)
    transaction_type = Column(String(20), nullable=False)
    amount = Column(Numeric(12, 2), nullable=False)
    transaction_date = Column(DateTime, default=datetime.utcnow)
    
    account = relationship("Account", back_populates="transactions")

    def __init__(self, account_id: int, transaction_type: str, amount: float):
        self.account_id = account_id
        self.transaction_type = transaction_type
        self.amount = amount


# File 3: Update User Model to Include Accounts Relationship in models/authentication/user_model.py