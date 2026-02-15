# Epic Title: Develop a User-Friendly Dashboard

from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from backend.app import db

class Account(db.Model):
    __tablename__ = 'accounts'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    account_number = Column(String(20), unique=True, nullable=False)
    account_type = Column(String(50), nullable=False)
    balance = Column(Float, nullable=False)

    user = relationship('User', backref='accounts')

    def __init__(self, user_id: int, account_number: str, account_type: str, balance: float):
        self.user_id = user_id
        self.account_number = account_number
        self.account_type = account_type
        self.balance = balance


# File 2: Transaction Model Definition in dashboard/models/transaction_model.py