# Epic Title: Core Banking System Integration

from backend.models.core_banking.transaction_model import Transaction
from backend.app import db

class TransactionRepository:
    @staticmethod
    def save(transaction: Transaction) -> None:
        db.session.add(transaction)
        db.session.commit()

    @staticmethod
    def get_by_user_id(user_id: int) -> list[Transaction]:
        return Transaction.query.filter_by(user_id=user_id).all()

    @staticmethod
    def get_by_external_id(external_id: str) -> Transaction | None:
        return Transaction.query.filter_by(external_id=external_id).first()

# File 6: Update Request Repository to Include External ID Handling in repositories/core_banking/request_repository.py (Modified)