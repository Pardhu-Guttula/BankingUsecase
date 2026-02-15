# Epic Title: Personalized Dashboard

from backend.models.dashboard.financial_activity_model import FinancialActivity
from backend.repositories.dashboard.financial_activity_repository import FinancialActivityRepository

class FinancialActivityService:
    @staticmethod
    def add_financial_activity(user_id: int, activity_type: str, amount: float, date: DateTime, description: str = None) -> FinancialActivity:
        financial_activity = FinancialActivity(user_id=user_id, activity_type=activity_type, amount=amount, date=date, description=description)
        FinancialActivityRepository.save(financial_activity)
        return financial_activity

    @staticmethod
    def get_user_financial_activities(user_id: int) -> list[FinancialActivity]:
        return FinancialActivityRepository.get_by_user_id(user_id)

# File 4: Financial Summary Controller in controllers/dashboard/financial_summary_controller.py