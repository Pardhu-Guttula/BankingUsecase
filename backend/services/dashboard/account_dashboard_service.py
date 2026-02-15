# Epic Title: Personalized Dashboard

from backend.models.dashboard.account_dashboard_model import AccountDashboard
from backend.repositories.dashboard.account_dashboard_repository import AccountDashboardRepository

class AccountDashboardService:
    @staticmethod
    def create_account_dashboard(user_id: int, account_number: str, account_type: str, balance: float) -> AccountDashboard:
        account_dashboard = AccountDashboard(user_id=user_id, account_number=account_number, account_type=account_type, balance=balance)
        AccountDashboardRepository.save(account_dashboard)
        return account_dashboard

    @staticmethod
    def get_user_account_dashboard(user_id: int) -> list[AccountDashboard]:
        return AccountDashboardRepository.get_by_user_id(user_id)

# File 4: Dashboard Controller to Handle User Requests in controllers/dashboard/account_dashboard_controller.py