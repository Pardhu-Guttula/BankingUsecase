# Epic Title: Personalized Dashboard

from backend.models.dashboard.dashboard_account_model import DashboardAccount
from backend.repositories.dashboard.dashboard_account_repository import DashboardAccountRepository


class DashboardAccountService:
    @staticmethod
    def create_dashboard_account(user_id: int, account_name: str, account_number: str, balance: int) -> DashboardAccount:
        dashboard_account = DashboardAccount(user_id=user_id, account_name=account_name, account_number=account_number, balance=balance)
        DashboardAccountRepository.save(dashboard_account)
        return dashboard_account

    @staticmethod
    def get_user_accounts(user_id: int) -> list[DashboardAccount]:
        return DashboardAccountRepository.get_accounts_by_user_id(user_id)


# File 4: Dashboard Controller to Display User Accounts and Transactions in dashboard/controllers/dashboard_controller.py