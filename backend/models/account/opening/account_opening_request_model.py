# Epic Title: Account Opening and Service Modifications

from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from backend.app import db

class AccountOpeningRequest(db.Model):
    __tablename__ = 'account_opening_requests'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    account_type = Column(String(50), nullable=False)
    initial_deposit = Column(Float, nullable=False)
    status = Column(String(20), default='pending', nullable=False)
    submitted_at = Column(DateTime, default=datetime.utcnow, nullable=False)

    user = relationship('User', back_populates='account_opening_requests')

    def __init__(self, user_id: int, account_type: str, initial_deposit: float, status: str = 'pending', submitted_at: DateTime = None):
        self.user_id = user_id
        self.account_type = account_type
        self.initial_deposit = initial_deposit
        self.status = status
        if submitted_at is None:
            submitted_at = datetime.utcnow()
        self.submitted_at = submitted_at


# File 2: Account Opening Repository in repositories/account/opening/account_opening_request_repository.py