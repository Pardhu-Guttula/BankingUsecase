# Epic Title: Develop a User-Friendly Dashboard

from dashboard.models.transaction_model import Transaction
from backend.app import db

class TransactionRepository:
    @staticmethod
    def get_transactions_by_account_id(account_id: int) -> list[Transaction]:
        return Transaction.query.filter_by(account_id=account_id).all()

    @staticmethod
    def save(transaction: Transaction) -> None:
        db.session.add(transaction)
        db.session.commit()


# File 5: Dashboard Service for Business Logic in dashboard/services/dashboard_service.py