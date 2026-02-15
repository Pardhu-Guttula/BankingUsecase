# Epic Title: Develop a User-Friendly Dashboard

from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey
from datetime import datetime
from backend.app import db

class Transaction(db.Model):
    __tablename__ = 'transactions'

    id = Column(Integer, primary_key=True)
    account_id = Column(Integer, ForeignKey('accounts.id'), nullable=False)
    amount = Column(Float, nullable=False)
    transaction_type = Column(String(50), nullable=False)
    timestamp = Column(DateTime, default=datetime.utcnow)

    account = relationship('Account', backref='transactions')

    def __init__(self, account_id: int, amount: float, transaction_type: str):
        self.account_id = account_id
        self.amount = amount
        self.transaction_type = transaction_type


# File 3: Account Repository for Database Operations in dashboard/repositories/account_repository.py