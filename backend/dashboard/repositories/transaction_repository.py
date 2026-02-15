# Epic Title: Personalized Dashboard

from backend.models.accounts.transaction_model import Transaction
from backend.app import db

class TransactionRepository:
    @staticmethod
    def save(transaction: Transaction) -> None:
        db.session.add(transaction)
        db.session.commit()

    @staticmethod
    def find_by_account_id(account_id: int) -> list[Transaction]:
        return Transaction.query.filter_by(account_id=account_id).all()


# File 6: Dashboard Service to Fetch User Account Data in dashboard/services/dashboard_service.py