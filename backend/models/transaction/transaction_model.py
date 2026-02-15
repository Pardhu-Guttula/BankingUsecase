# Epic Title: Develop a User-Friendly Dashboard

from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from backend.app import db
from datetime import datetime

class Transaction(db.Model):
    __tablename__ = 'transactions'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    account_id = Column(Integer, ForeignKey('accounts.id'), nullable=False)
    transaction_type = Column(String(50), nullable=False)
    amount = Column(Integer, nullable=False)
    timestamp = Column(DateTime, default=datetime.utcnow)

    def __init__(self, user_id: int, account_id: int, transaction_type: str, amount: int):
        self.user_id = user_id
        self.account_id = account_id
        self.transaction_type = transaction_type
        self.amount = amount


# File 7: Update app.py to Register Dashboard Controller Blueprint