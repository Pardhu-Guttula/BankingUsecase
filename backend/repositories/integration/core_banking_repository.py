# Epic Title: Develop Secure APIs

from backend.models.integration.core_banking_model import CoreBankingTransaction
from backend.app import db

class CoreBankingRepository:
    @staticmethod
    def save(transaction: CoreBankingTransaction) -> None:
        db.session.add(transaction)
        db.session.commit()

    @staticmethod
    def find_by_transaction_id(transaction_id: str) -> CoreBankingTransaction:
        return CoreBankingTransaction.query.filter_by(transaction_id=transaction_id).first()

    @staticmethod
    def find_all() -> list[CoreBankingTransaction]:
        return CoreBankingTransaction.query.all()


# File 3: Core Banking System Integration Service in `services/integration/core_banking_service.py`