# Epic Title: Account Opening and Service Modifications

from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from backend.app import db

class AccountOpeningRequest(db.Model):
    __tablename__ = 'account_opening_requests'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    account_type = Column(String(20), nullable=False)
    status = Column(String(20), nullable=False, default='pending')
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, onupdate=datetime.utcnow)

    user = relationship("User", back_populates="account_opening_requests")

    def __init__(self, user_id: int, account_type: str, status: str = 'pending'):
        self.user_id = user_id
        self.account_type = account_type
        self.status = status


# File 2: Update User Model to Include Relationship with AccountOpeningRequest in models/authentication/user_model.py