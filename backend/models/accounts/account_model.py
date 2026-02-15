# Epic Title: Personalized Dashboard

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from backend.app import db

class Account(db.Model):
    __tablename__ = 'accounts'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    account_number = Column(String(20), unique=True, nullable=False)
    account_type = Column(String(50), nullable=False)
    balance = Column(Integer, nullable=False)

    user = relationship('User', back_populates='accounts')
    transactions = relationship('Transaction', back_populates='account')

    def __init__(self, user_id: int, account_number: str, account_type: str, balance: int):
        self.user_id = user_id
        self.account_number = account_number
        self.account_type = account_type
        self.balance = balance