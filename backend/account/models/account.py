# Epic Title: Develop a User-Friendly Dashboard

from sqlalchemy import Column, Integer, String, ForeignKey, DECIMAL
from sqlalchemy.orm import relationship, declarative_base

Base = declarative_base()

class Account(Base):
    __tablename__ = 'accounts'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    account_number = Column(String(30), unique=True, nullable=False)
    account_type = Column(String(20), nullable=False)
    balance = Column(DECIMAL(10, 2), default=0)

    user = relationship('User', back_populates='accounts')

    def __repr__(self) -> str:
        return f"<Account(user_id='{self.user_id}', account_number='{self.account_number}', account_type='{self.account_type}', balance='{self.balance}')>"



# File 3: Transaction Model in account/models/transaction.py