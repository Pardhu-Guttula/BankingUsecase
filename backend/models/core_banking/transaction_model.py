# Epic Title: Core Banking System Integration

from sqlalchemy import Column, Integer, Float, DateTime, ForeignKey
from backend.app import db
import datetime

class CoreBankingTransaction(db.Model):
    __tablename__ = 'core_banking_transactions'

    id = Column(Integer, primary_key=True)
    account_id = Column(Integer, ForeignKey('core_banking_accounts.id'), nullable=False)
    amount = Column(Float, nullable=False)
    timestamp = Column(DateTime, default=datetime.datetime.utcnow, nullable=False)

    def __init__(self, account_id: int, amount: float):
        self.account_id = account_id
        self.amount = amount


# File 3: Core Banking Account Repository in repositories/core_banking/account_repository.py