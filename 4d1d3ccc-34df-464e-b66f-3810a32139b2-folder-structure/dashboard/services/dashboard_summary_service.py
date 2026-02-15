# Epic Title: Overview of Financial Activities

from dashboard.repositories.account_repository import AccountRepository
from dashboard.repositories.transaction_repository import TransactionRepository

class DashboardSummaryService:
    @staticmethod
    def get_financial_summary(user_id: int) -> dict:
        accounts = AccountRepository.get_accounts_by_user_id(user_id)
        total_balance = sum(account.balance for account in accounts)

        transactions = []
        for account in accounts:
            transactions.extend(TransactionRepository.get_transactions_by_account_id(account.id))

        total_transactions = len(transactions)
        income = sum(txn.amount for txn in transactions if txn.transaction_type == 'credit')
        expenses = sum(txn.amount for txn in transactions if txn.transaction_type == 'debit')

        summary = {
            "total_balance": total_balance,
            "total_accounts": len(accounts),
            "total_transactions": total_transactions,
            "total_income": income,
            "total_expenses": expenses
        }

        return summary


# File 2: Dashboard Summary Controller for Handling Requests in dashboard/controllers/dashboard_summary_controller.py