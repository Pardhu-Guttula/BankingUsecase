# Epic Title: Personalized Dashboard

from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from datetime import datetime
from backend.app import db


class DashboardAccount(db.Model):
    __tablename__ = 'dashboard_accounts'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    account_name = Column(String(255), nullable=False)
    account_number = Column(String(255), nullable=False)
    balance = Column(Integer, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)

    def __init__(self, user_id: int, account_name: str, account_number: str, balance: int, created_at: DateTime = None):
        self.user_id = user_id
        self.account_name = account_name
        self.account_number = account_number
        self.balance = balance
        if created_at is None:
            created_at = datetime.utcnow()
        self.created_at = created_at


# File 2: Dashboard Account Repository in repositories/dashboard/dashboard_account_repository.py