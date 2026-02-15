# Epic Title: Personalized Dashboard

from backend.repositories.accounts.account_repository import AccountRepository
from backend.repositories.accounts.transaction_repository import TransactionRepository
from backend.models.accounts.account_model import Account
from backend.models.accounts.transaction_model import Transaction

class DashboardService:
    @staticmethod
    def get_user_accounts(user_id: int) -> list[Account]:
        return AccountRepository.get_accounts_by_user(user_id)

    @staticmethod
    def get_account_transactions(account_id: int) -> list[Transaction]:
        return TransactionRepository.get_transactions_by_account(account_id)


# File 6: Controller to handle Dashboard requests in controllers/dashboard/