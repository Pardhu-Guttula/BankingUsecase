# Epic Title: Personalized Dashboard

from backend.models.accounts.transaction_model import Transaction
from backend.app import db

class TransactionRepository:
    @staticmethod
    def find_by_account_id(account_id: int) -> list[Transaction]:
        return Transaction.query.filter_by(account_id=account_id).all()


# File 4: Dashboard Controller to Display Personalized Dashboard in dashboard/controllers/dashboard_controller.py