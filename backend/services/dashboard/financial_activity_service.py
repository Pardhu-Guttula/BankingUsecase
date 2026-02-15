# Epic Title: Overview of Financial Activities

from backend.repositories.dashboard.financial_activity_repository import FinancialActivityRepository
from backend.models.dashboard.financial_activity_model import FinancialActivity

class FinancialActivityService:
    @staticmethod
    def get_financial_summary(user_id: int) -> list:
        return FinancialActivityRepository.find_by_user_id(user_id)


# File 4: Dashboard Controller Updated for Financial Summary in controllers/dashboard/dashboard_controller.py