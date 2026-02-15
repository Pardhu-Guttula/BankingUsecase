# Epic Title: Develop a User-Friendly Dashboard

from dashboard.repositories.account_repository import AccountRepository
from dashboard.repositories.transaction_repository import TransactionRepository

class DashboardService:
    @staticmethod
    def get_user_accounts(user_id: int) -> list:
        accounts = AccountRepository.get_accounts_by_user_id(user_id)
        return [{
            "account_number": account.account_number,
            "account_type": account.account_type,
            "balance": account.balance
        } for account in accounts]

    @staticmethod
    def get_account_transactions(account_id: int) -> list:
        transactions = TransactionRepository.get_transactions_by_account_id(account_id)
        return [{
            "amount": transaction.amount,
            "transaction_type": transaction.transaction_type,
            "timestamp": transaction.timestamp
        } for transaction in transactions]


# File 6: Dashboard Controller for Handling Requests in dashboard/controllers/dashboard_controller.py