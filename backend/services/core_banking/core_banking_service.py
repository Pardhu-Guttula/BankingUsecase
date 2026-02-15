# Epic Title: Core Banking System Integration

from backend.models.core_banking.transaction_model import Transaction
from backend.models.core_banking.request_model import Request
from backend.repositories.core_banking.transaction_repository import TransactionRepository
from backend.repositories.core_banking.request_repository import RequestRepository

class CoreBankingService:
    @staticmethod
    def create_transaction(user_id: int, data: dict) -> Transaction:
        transaction = Transaction(user_id=user_id, amount=data['amount'], status='pending')
        TransactionRepository.save(transaction)
        return transaction

    @staticmethod
    def create_request(user_id: int, data: dict) -> Request:
        request = Request(user_id=user_id, type=data['type'], status='pending')
        RequestRepository.save(request)
        return request

# File 4: Transaction Model in models/core_banking/transaction_model.py