# Epic Title: Personalized Dashboard

from backend.repositories.accounts.transaction_repository import TransactionRepository
from backend.models.accounts.transaction_model import Transaction
from datetime import datetime

class TransactionService:
    @staticmethod
    def get_account_transactions(account_id: int) -> list[Transaction]:
        return TransactionRepository.get_transactions_by_account(account_id)

    @staticmethod
    def create_transaction(account_id: int, amount: float, transaction_type: str) -> Transaction:
        transaction = Transaction(account_id=account_id, amount=amount, transaction_type=transaction_type, timestamp=datetime.utcnow())
        TransactionRepository.save(transaction)
        return transaction

    @staticmethod
    def update_transaction(transaction_id: int, amount: float = None, transaction_type: str = None) -> Transaction:
        transaction = Transaction.query.get(transaction_id)
        if amount is not None:
            transaction.amount = amount
        if transaction_type is not None:
            transaction.transaction_type = transaction_type
        TransactionRepository.update(transaction)
        return transaction

    @staticmethod
    def delete_transaction(transaction_id: int) -> None:
        transaction = Transaction.query.get(transaction_id)
        TransactionRepository.delete(transaction)


# File 7: Dashboard Controller to Display Financial Summary in dashboard/controllers/dashboard_controller.py (Already Exists, Modified)