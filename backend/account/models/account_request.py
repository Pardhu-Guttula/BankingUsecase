# Epic Title: Streamline Account Opening Requests

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()

class AccountRequest(Base):
    __tablename__ = 'account_requests'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    account_type = Column(String(50), nullable=False)
    status = Column(String(20), default='pending')

    user = relationship('User', back_populates='account_requests')

    def __repr__(self) -> str:
        return f"<AccountRequest(user_id='{self.user_id}', account_type='{self.account_type}', status='{self.status}')>"



# File 2: Updated User Model in account/models/user.py