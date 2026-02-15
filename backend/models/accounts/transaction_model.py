# Epic Title: Personalized Dashboard

from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from backend.app import db
import datetime

class Transaction(db.Model):
    __tablename__ = 'transactions'

    id = Column(Integer, primary_key=True)
    account_id = Column(Integer, ForeignKey('accounts.id'), nullable=False)
    amount = Column(Integer, nullable=False)
    type = Column(String(50), nullable=False)
    date = Column(DateTime, default=datetime.datetime.utcnow, nullable=False)
    description = Column(String(255), nullable=True)

    account = relationship('Account', back_populates='transactions')

    def __init__(self, account_id: int, amount: int, type: str, description: str = None):
        self.account_id = account_id
        self.amount = amount
        self.type = type
        self.description = description


# File 3: Financial Summary Repository for Retrieving Summary Data in repositories/dashboard/financial_summary_repository.py