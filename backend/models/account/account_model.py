# Epic Title: Personalized Dashboard

from sqlalchemy import Column, Integer, String, DECIMAL, ForeignKey
from sqlalchemy.orm import relationship
from backend.app import db

class Account(db.Model):
    __tablename__ = 'accounts'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    account_number = Column(String(20), unique=True, nullable=False)
    balance = Column(DECIMAL(10, 2), nullable=False)
    account_type = Column(String(20), nullable=False)
    user = relationship('User', back_populates='accounts')
    transactions = relationship('Transaction', back_populates='account')


# File 6: Transaction Model in models/account/transaction_model.py (Existing File, Re-emitting for Context)