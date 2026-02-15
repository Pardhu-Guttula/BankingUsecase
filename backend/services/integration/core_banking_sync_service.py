# Epic Title: Core Banking System Integration

from backend.repositories.core_banking.transaction_repository import TransactionRepository
from backend.repositories.core_banking.request_repository import RequestRepository
from backend.models.core_banking.transaction_model import Transaction
from backend.models.core_banking.request_model import Request

class CoreBankingSyncService:
    @staticmethod
    def sync_transactions(external_transactions: list[dict]) -> None:
        for ext_trans in external_transactions:
            existing_trans = TransactionRepository.get_by_external_id(ext_trans['external_id'])
            if existing_trans:
                CoreBankingSyncService.update_transaction(existing_trans, ext_trans)
            else:
                CoreBankingSyncService.create_transaction(ext_trans)

    @staticmethod
    def sync_requests(external_requests: list[dict]) -> None:
        for ext_req in external_requests:
            existing_req = RequestRepository.get_by_external_id(ext_req['external_id'])
            if existing_req:
                CoreBankingSyncService.update_request(existing_req, ext_req)
            else:
                CoreBankingSyncService.create_request(ext_req)

    @staticmethod
    def create_transaction(data: dict) -> Transaction:
        transaction = Transaction(
            user_id=data['user_id'],
            amount=data['amount'],
            status=data['status'],
            external_id=data['external_id']
        )
        TransactionRepository.save(transaction)
        return transaction

    @staticmethod
    def update_transaction(transaction: Transaction, data: dict) -> None:
        transaction.amount = data['amount']
        transaction.status = data['status']
        TransactionRepository.save(transaction)

    @staticmethod
    def create_request(data: dict) -> Request:
        request = Request(
            user_id=data['user_id'],
            type=data['type'],
            status=data['status'],
            external_id=data['external_id']
        )
        RequestRepository.save(request)
        return request

    @staticmethod
    def update_request(request: Request, data: dict) -> None:
        request.type = data['type']
        request.status = data['status']
        RequestRepository.save(request)

# File 2: Sync Controller in controllers/integration/core_banking_sync_controller.py