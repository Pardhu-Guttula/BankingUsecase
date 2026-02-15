# Epic Title: Personalized Dashboard

from backend.models.dashboard.financial_activity_model import FinancialActivity
from backend.app import db

class FinancialActivityRepository:
    @staticmethod
    def save(financial_activity: FinancialActivity) -> None:
        db.session.add(financial_activity)
        db.session.commit()

    @staticmethod
    def get_by_user_id(user_id: int) -> list[FinancialActivity]:
        return FinancialActivity.query.filter_by(user_id=user_id).all()

# File 3: Financial Activity Service in services/dashboard/financial_activity_service.py