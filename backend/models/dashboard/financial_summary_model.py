# Epic Title: Personalized Dashboard

from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Float
from datetime import datetime
from backend.app import db


class FinancialSummary(db.Model):
    __tablename__ = 'financial_summaries'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    total_balance = Column(Float, nullable=False)
    total_transactions = Column(Integer, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)

    def __init__(self, user_id: int, total_balance: float, total_transactions: int, created_at: DateTime = None):
        self.user_id = user_id
        self.total_balance = total_balance
        self.total_transactions = total_transactions
        if created_at is None:
            created_at = datetime.utcnow()
        self.created_at = created_at


# File 2: Financial Summary Repository in repositories/dashboard/financial_summary_repository.py