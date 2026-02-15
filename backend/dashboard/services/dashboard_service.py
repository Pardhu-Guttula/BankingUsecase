# Epic Title: Personalized Dashboard

from backend.dashboard.repositories.account_repository import AccountRepository
from backend.dashboard.repositories.transaction_repository import TransactionRepository
from backend.models.accounts.account_model import Account
from backend.models.accounts.transaction_model import Transaction

class DashboardService:
    @staticmethod
    def get_user_accounts(user_id: int) -> list[Account]:
        return AccountRepository.find_by_user_id(user_id)

    @staticmethod
    def get_account_transactions(account_id: int) -> list[Transaction]:
        return TransactionRepository.find_by_account_id(account_id)


# File 7: Dashboard Controller to Render User Dashboard in dashboard/controllers/dashboard_controller.py