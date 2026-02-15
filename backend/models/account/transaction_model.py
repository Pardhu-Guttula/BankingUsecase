# Epic Title: Personalized Dashboard

from sqlalchemy import Column, Integer, String, DECIMAL, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from backend.app import db
import datetime

class Transaction(db.Model):
    __tablename__ = 'transactions'

    id = Column(Integer, primary_key=True)
    account_id = Column(Integer, ForeignKey('accounts.id'), nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    amount = Column(DECIMAL(10, 2), nullable=False)
    timestamp = Column(DateTime, default=datetime.datetime.utcnow, nullable=False)
    description = Column(String(255), nullable=True)
    account = relationship('Account', back_populates='transactions')
    user = relationship('User', back_populates='transactions')


# File 7: Update Main App to Register Dashboard Controller in app.py (Existing File, Re-emitting for Context)