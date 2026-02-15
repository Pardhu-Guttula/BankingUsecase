# Epic Title: Streamline Account Opening Requests

from sqlalchemy import Column, Integer, String, DateTime, Boolean, ForeignKey
from datetime import datetime
from backend.app import db

class AccountOpeningRequest(db.Model):
    __tablename__ = 'account_opening_requests'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    account_type = Column(String(50), nullable=False)
    status = Column(String(50), default='pending', nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)

    user = db.relationship('User', backref='requests')

    def __init__(self, user_id: int, account_type: str):
        self.user_id = user_id
        self.account_type = account_type


# File 2: Account Opening Request Repository for Database Operations in dashboard/repositories/account_opening_request_repository.py