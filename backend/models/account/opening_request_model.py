# Epic Title: Account Opening and Service Modifications

from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from datetime import datetime
from backend.app import db

class OpeningRequest(db.Model):
    __tablename__ = 'opening_requests'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    account_type = Column(String(100), nullable=False)
    status = Column(String(50), nullable=False, default="pending")
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)

    def __init__(self, user_id: int, account_type: str, status: str = "pending"):
        self.user_id = user_id
        self.account_type = account_type
        self.status = status

# File 2: Account Opening Request Repository in repositories/account/opening_request_repository.py