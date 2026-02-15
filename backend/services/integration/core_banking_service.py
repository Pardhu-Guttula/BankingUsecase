# Epic Title: Develop Secure APIs

from backend.repositories.integration.core_banking_repository import CoreBankingRepository
from backend.models.integration.core_banking_model import CoreBankingTransaction
import requests

class CoreBankingService:
    @staticmethod
    def initiate_transaction(transaction_id: str, amount: int, transaction_type: str, status: str) -> None:
        transaction = CoreBankingTransaction(transaction_id=transaction_id, amount=amount, transaction_type=transaction_type, status=status)
        CoreBankingRepository.save(transaction)
        # Example integration logic
        response = requests.post('https://core-banking-system/api/transactions', json={
            'transaction_id': transaction_id,
            'amount': amount,
            'transaction_type': transaction_type,
            'status': status
        }, headers={
            'Authorization': 'Bearer your_api_token'
        })
        if response.status_code != 200:
            raise Exception('Error integrating with core banking system')

    @staticmethod
    def get_transaction_by_id(transaction_id: str) -> CoreBankingTransaction:
        return CoreBankingRepository.find_by_transaction_id(transaction_id)

    @staticmethod
    def get_all_transactions() -> list[CoreBankingTransaction]:
        return CoreBankingRepository.find_all()


# File 4: Core Banking System Integration Controller in `controllers/integration/core_banking_controller.py`