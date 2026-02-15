# Epic Title: Overview of Financial Activities

from sqlalchemy import Column, Integer, String, ForeignKey, Float
from backend.app import db

class FinancialActivity(db.Model):
    __tablename__ = 'financial_activities'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    activity_type = Column(String(50), nullable=False)
    amount = Column(Float, nullable=False)
    description = Column(String(255), nullable=True)

    def __init__(self, user_id: int, activity_type: str, amount: float, description: str = None):
        self.user_id = user_id
        self.activity_type = activity_type
        self.amount = amount
        self.description = description


# File 2: Financial Activities Repository in repositories/dashboard/financial_activity_repository.py