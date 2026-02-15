# Epic Title: Develop a User-Friendly Dashboard

from backend.models.transaction.transaction_model import Transaction
from backend.app import db

class TransactionRepository:
    @staticmethod
    def find_by_user_id(user_id: int) -> list[Transaction]:
        return Transaction.query.filter_by(user_id=user_id).all()


# File 5: Account Model in models/accounts/account_model.py