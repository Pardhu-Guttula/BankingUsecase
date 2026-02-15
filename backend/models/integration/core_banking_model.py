# Epic Title: Develop Secure APIs

from sqlalchemy import Column, Integer, String, DateTime
from backend.app import db
from datetime import datetime

class CoreBankingTransaction(db.Model):
    __tablename__ = 'core_banking_transactions'

    id = Column(Integer, primary_key=True)
    transaction_id = Column(String(255), nullable=False, unique=True)
    amount = Column(Integer, nullable=False)
    transaction_type = Column(String(50), nullable=False)
    status = Column(String(50), nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)

    def __init__(self, transaction_id: str, amount: int, transaction_type: str, status: str):
        self.transaction_id = transaction_id
        self.amount = amount
        self.transaction_type = transaction_type
        self.status = status
        self.created_at = datetime.utcnow()


# File 2: Core Banking System Integration Repository in `repositories/integration/core_banking_repository.py`