# Epic Title: Personalized Dashboard

from backend.repositories.dashboard.financial_summary_repository import FinancialSummaryRepository

class FinancialSummaryService:
    @staticmethod
    def get_account_summary(user_id: int):
        return FinancialSummaryRepository.get_account_summary(user_id)

    @staticmethod
    def get_transaction_summary(user_id: int):
        return FinancialSummaryRepository.get_transaction_summary(user_id)


# File 5: Controller to handle Financial Summary in controllers/dashboard/financial_summary_controller.py