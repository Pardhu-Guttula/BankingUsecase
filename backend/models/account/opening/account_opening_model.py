# Epic Title: Account Opening and Service Modifications

from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from backend.app import db
from datetime import datetime

class AccountOpening(db.Model):
    __tablename__ = 'account_openings'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    account_type = Column(String(50), nullable=False)
    status = Column(String(50), nullable=False, default='Pending')
    submitted_at = Column(DateTime, nullable=False, default=datetime.utcnow)

    user = relationship('User', backref='account_openings')

    def __init__(self, user_id: int, account_type: str, status: str = 'Pending'):
        self.user_id = user_id
        self.account_type = account_type
        self.status = status

# File 2: Account Opening Repository in repositories/account/opening/account_opening_repository.py