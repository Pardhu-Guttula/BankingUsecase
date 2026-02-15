# Epic Title: Account Opening and Service Modifications

from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from backend.app import db
from datetime import datetime

class AccountOpeningRequest(db.Model):
    __tablename__ = 'account_opening_requests'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    request_date = Column(DateTime, nullable=False, default=datetime.utcnow)
    account_type = Column(String(50), nullable=False)
    status = Column(String(50), nullable=False, default='pending')

    def __init__(self, user_id: int, account_type: str, status: str = 'pending'):
        self.user_id = user_id
        self.account_type = account_type
        self.status = status

# File 2: Account Opening Request Repository in repositories/account/opening_requests/account_opening_request_repository.py