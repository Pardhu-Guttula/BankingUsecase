# Epic Title: Personalized Dashboard

from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from backend.app import db

class FinancialActivity(db.Model):
    __tablename__ = 'financial_activities'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    activity_type = Column(String(50), nullable=False)
    amount = Column(Float, nullable=False)
    date = Column(DateTime, nullable=False)
    description = Column(String(255), nullable=True)

    user = relationship('User', backref='financial_activities')

    def __init__(self, user_id: int, activity_type: str, amount: float, date: DateTime, description: str = None):
        self.user_id = user_id
        self.activity_type = activity_type
        self.amount = amount
        self.date = date
        self.description = description

# File 2: Financial Activity Repository in repositories/dashboard/financial_activity_repository.py