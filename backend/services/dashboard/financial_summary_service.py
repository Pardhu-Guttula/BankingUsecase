# Epic Title: Personalized Dashboard

from backend.repositories.dashboard.dashboard_repository import DashboardRepository
from backend.models.dashboard.dashboard_model import Account, Transaction

class FinancialSummaryService:
    @staticmethod
    def get_financial_summary(user_id: int) -> dict:
        accounts = DashboardRepository.get_user_accounts(user_id)
        total_balance = sum(account.balance for account in accounts)
        transactions = []

        for account in accounts:
            account_transactions = DashboardRepository.get_account_transactions(account.id)
            transactions.extend(account_transactions)

        transaction_summary = {
            'total_balance': total_balance,
            'total_transactions': len(transactions),
            'transactions': [{'account_number': t.account.account_number,
                              'amount': t.amount,
                              'transaction_type': t.transaction_type,
                              'timestamp': t.timestamp} for t in transactions]
        }

        return transaction_summary

# File 2: Financial Summary Controller in controllers/dashboard/financial_summary_controller.py