# Epic Title: Core Banking System Integration

from backend.models.core_banking.transaction_model import CoreBankingTransaction
from backend.app import db

class TransactionRepository:
    @staticmethod
    def get_transaction_by_id(transaction_id: int) -> CoreBankingTransaction:
        return CoreBankingTransaction.query.get(transaction_id)

    @staticmethod
    def get_transactions_by_account_id(account_id: int) -> list[CoreBankingTransaction]:
        return CoreBankingTransaction.query.filter_by(account_id=account_id).all()

    @staticmethod
    def save(transaction: CoreBankingTransaction) -> None:
        db.session.add(transaction)
        db.session.commit()

    @staticmethod
    def update(transaction: CoreBankingTransaction) -> None:
        db.session.commit()


# File 5: Core Banking Sync Service in services/core_banking/core_banking_sync_service.py