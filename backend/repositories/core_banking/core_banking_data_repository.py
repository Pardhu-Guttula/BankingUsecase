# Epic Title: Core Banking System Integration

from backend.models.core_banking.core_banking_model import CoreBankingData
from backend.app import db

class CoreBankingDataRepository:
    @staticmethod
    def save_data(data: dict) -> None:
        for record in data:
            core_banking_data = CoreBankingData(
                account_id=record['account_id'],
                balance=record['balance'],
                status=record['status']
            )
            db.session.add(core_banking_data)
        db.session.commit()

# File 4: Core Banking Data Sync Controller in integration/controllers/core_banking_data_sync_controller.py