# Epic Title: Streamline Account Opening Requests

from sqlalchemy import Column, Integer, String, DateTime, Boolean, ForeignKey
from backend.app import db
from datetime import datetime

class AccountOpeningRequest(db.Model):
    __tablename__ = 'account_opening_requests'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    account_type = Column(String(50), nullable=False)
    status = Column(String(50), nullable=False, default='Pending')
    submission_date = Column(DateTime, default=datetime.utcnow)
    approved = Column(Boolean, default=False)

    def __init__(self, user_id: int, account_type: str):
        self.user_id = user_id
        self.account_type = account_type
        self.status = 'Pending'
        self.submission_date = datetime.utcnow()
        self.approved = False


# File 2: Account Opening Request Repository in repositories/account/opening_requests/account_opening_request_repository.py