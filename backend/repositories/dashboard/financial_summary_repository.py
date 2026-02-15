# Epic Title: Personalized Dashboard

from backend.models.accounts.account_model import Account
from backend.models.accounts.transaction_model import Transaction
from backend.app import db

class FinancialSummaryRepository:
    @staticmethod
    def get_account_summary(user_id: int) -> list[Account]:
        return Account.query.filter_by(user_id=user_id).all()

    @staticmethod
    def get_transaction_summary(user_id: int) -> list[Transaction]:
        return db.session.query(Transaction).join(Account).filter(Account.user_id == user_id).all()


# File 4: Service Layer for Financial Summary in services/dashboard/financial_summary_service.py