# Epic Title: Personalized Dashboard

from typing import Dict
from backend.repositories.account.account_repository import AccountRepository
from backend.repositories.transaction.transaction_repository import TransactionRepository

class FinancialSummaryService:
    @staticmethod
    def get_financial_summary(user_id: int) -> Dict:
        accounts = AccountRepository.get_user_accounts(user_id)
        transactions = TransactionRepository.get_recent_transactions(user_id)
        total_balance = sum(account.balance for account in accounts)
        total_transactions = len(transactions)
        return {
            "total_balance": total_balance,
            "total_transactions": total_transactions,
            "accounts_summary": [{"account_number": account.account_number, "balance": account.balance} for account in accounts],
            "transactions_summary": [{"amount": txn.amount, "timestamp": txn.timestamp, "description": txn.description} for txn in transactions]
        }


# File 2: Dashboard Controller to Integrate Financial Summary in dashboard/controllers/dashboard_controller.py