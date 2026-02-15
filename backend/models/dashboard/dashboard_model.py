# Epic Title: Personalized Dashboard

from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Float
from sqlalchemy.orm import relationship
from backend.app import db
from datetime import datetime

class Account(db.Model):
    __tablename__ = 'accounts'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    account_number = Column(String(50), unique=True, nullable=False)
    balance = Column(Float, nullable=False, default=0.0)
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow)

    user = relationship('User', backref='accounts')

    def __init__(self, user_id: int, account_number: str, balance: float = 0.0):
        self.user_id = user_id
        self.account_number = account_number
        self.balance = balance

class Transaction(db.Model):
    __tablename__ = 'transactions'

    id = Column(Integer, primary_key=True)
    account_id = Column(Integer, ForeignKey('accounts.id'), nullable=False)
    amount = Column(Float, nullable=False)
    transaction_type = Column(String(50), nullable=False)
    timestamp = Column(DateTime, nullable=False, default=datetime.utcnow)

    account = relationship('Account', backref='transactions')

    def __init__(self, account_id: int, amount: float, transaction_type: str):
        self.account_id = account_id
        self.amount = amount
        self.transaction_type = transaction_type

# File 2: Dashboard Repository in repositories/dashboard/dashboard_repository.py