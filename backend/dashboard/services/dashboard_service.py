# Epic Title: Develop a User-Friendly Dashboard

from backend.repositories.accounts.account_repository import AccountRepository
from backend.repositories.transaction.transaction_repository import TransactionRepository

class DashboardService:
    @staticmethod
    def get_user_accounts(user_id: int) -> list:
        return AccountRepository.find_by_user_id(user_id)

    @staticmethod
    def get_user_transactions(user_id: int) -> list:
        return TransactionRepository.find_by_user_id(user_id)


# File 3: Account Repository in repositories/accounts/account_repository.py