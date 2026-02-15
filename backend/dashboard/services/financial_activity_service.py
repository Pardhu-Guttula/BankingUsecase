# Epic Title: Personalized Dashboard

from backend.dashboard.repositories.account_repository import AccountRepository
from backend.dashboard.repositories.transaction_repository import TransactionRepository
from backend.models.accounts.account_model import Account
from backend.models.accounts.transaction_model import Transaction

class FinancialActivityService:
    @staticmethod
    def get_account_summary(user_id: int) -> list[Account]:
        return AccountRepository.find_by_user_id(user_id)

    @staticmethod
    def get_transaction_summary(account_id: int) -> list[Transaction]:
        return TransactionRepository.find_by_account_id(account_id)

    @staticmethod
    def get_financial_activity_summary(user_id: int) -> dict:
        accounts = FinancialActivityService.get_account_summary(user_id)
        account_summaries = [
            {
                "account_number": account.account_number,
                "account_type": account.account_type,
                "balance": account.balance,
                "transactions": FinancialActivityService.get_transaction_summary(account.id)
            }
            for account in accounts
        ]
        return {"accounts": account_summaries}


# File 2: Update Dashboard Service to Include Financial Activity Summary in dashboard/services/dashboard_service.py