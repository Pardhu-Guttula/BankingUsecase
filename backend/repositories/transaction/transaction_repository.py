# Epic Title: Personalized Dashboard

from typing import List
from backend.models.account.transaction_model import Transaction
from backend.app import db

class TransactionRepository:
    @staticmethod
    def get_recent_transactions(user_id: int) -> List[Transaction]:
        return Transaction.query.filter_by(user_id=user_id).order_by(Transaction.timestamp.desc()).limit(10).all()


# File 5: Account Model in models/account/account_model.py