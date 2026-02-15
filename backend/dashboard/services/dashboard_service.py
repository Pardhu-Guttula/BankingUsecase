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

    @staticmethod
    def get_summary(user_id: int) -> dict:
        accounts = AccountRepository.find_by_user_id(user_id)
        summary = {"accounts": [], "total_balance": 0, "transactions": []}
        for account in accounts:
            account_info = {
                "account_number": account.account_number,
                "account_type": account.account_type,
                "balance": account.balance
            }
            summary["accounts.append(account_info)
            summary["total_balance"] += account.balance
            transactions = TransactionRepository.find_by_account_id(account.id)
            for txn in transactions:
                txn_info = {
                    "transaction_type": txn.transaction_type,
                    "amount": txn.amount,
                    "transaction_date": txn.transaction_date
                }
                summary["transactions"].append(txn_info)
        return summary


# File 2: Dashboard Controller to Provide Account Summary in dashboard/controllers/dashboard_controller.py