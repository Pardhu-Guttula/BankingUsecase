# Epic Title: Core Banking System Integration

from sqlalchemy import Column, Integer, String, Float, DateTime
from backend.app import db
import datetime

class CoreBankingAccount(db.Model):
    __tablename__ = 'core_banking_accounts'

    id = Column(Integer, primary_key=True)
    account_number = Column(String(20), unique=True, nullable=False)
    balance = Column(Float, nullable=False)
    last_synced = Column(DateTime, default=datetime.datetime.utcnow, nullable=False)

    def __init__(self, account_number: str, balance: float):
        self.account_number = account_number
        self.balance = balance


# File 2: Core Banking Transaction Model in models/core_banking/transaction_model.py