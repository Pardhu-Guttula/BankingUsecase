# Epic Title: Develop a User-Friendly Dashboard

from sqlalchemy import Column, Integer, String, ForeignKey, DECIMAL, DateTime
from sqlalchemy.orm import relationship, declarative_base
from datetime import datetime

Base = declarative_base()

class Transaction(Base):
    __tablename__ = 'transactions'

    id = Column(Integer, primary_key=True)
    account_id = Column(Integer, ForeignKey('accounts.id'), nullable=False)
    amount = Column(DECIMAL(10, 2), nullable=False)
    transaction_type = Column(String(30), nullable=False)  # e.g., credit or debit
    created_at = Column(DateTime, default=datetime.utcnow)

    account = relationship('Account', back_populates='transactions')

    def __repr__(self) -> str:
        return f"<Transaction(account_id='{self.account_id}', amount='{self.amount}', transaction_type='{self.transaction_type}', created_at='{self.created_at}')>"



# File 4: Update User Model for Associations in account/models/user.py