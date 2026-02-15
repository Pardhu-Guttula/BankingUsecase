# Epic Title: Core Banking System Integration

from sqlalchemy import Column, Integer, String, DateTime, Float
from datetime import datetime
from backend.app import db

class CoreBankingData(db.Model):
    __tablename__ = 'core_banking_data'

    id = Column(Integer, primary_key=True)
    account_id = Column(Integer, nullable=False)
    balance = Column(Float, nullable=False)
    status = Column(String(50), nullable=False)
    last_updated = Column(DateTime, default=datetime.utcnow, nullable=False)
    
    def __init__(self, account_id: int, balance: float, status: str):
        self.account_id = account_id
        self.balance = balance
        self.status = status
        self.last_updated = datetime.utcnow()

# File 3: Core Banking Data Repository in repositories/core_banking/core_banking_data_repository.py