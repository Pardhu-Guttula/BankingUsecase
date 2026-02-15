# Epic Title: Overview of Financial Activities

from backend.models.dashboard.financial_activity_model import FinancialActivity
from backend.app import db

class FinancialActivityRepository:
    @staticmethod
    def save(activity: FinancialActivity) -> None:
        db.session.add(activity)
        db.session.commit()

    @staticmethod
    def find_by_user_id(user_id: int) -> list[FinancialActivity]:
        return FinancialActivity.query.filter_by(user_id=user_id).all()


# File 3: Financial Activities Service in backend/services/dashboard/financial_activity_service.py