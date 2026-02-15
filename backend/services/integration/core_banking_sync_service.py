# Epic Title: Data Synchronization Mechanisms

from backend.repositories.integration.core_banking_sync_repository import CoreBankingSyncRepository
from backend.models.integration.core_banking_sync_model import CoreBankingSync
from datetime import datetime
import requests

class CoreBankingSyncService:
    @staticmethod
    def sync_entity(entity: str) -> None:
        sync_record = CoreBankingSyncRepository.find_by_entity(entity)
        if not sync_record:
            sync_record = CoreBankingSync(entity=entity)
            CoreBankingSyncRepository.save(sync_record)

        # Example logic to synchronize data with core banking system
        response = requests.get(f'https://core-banking-system/api/{entity}/sync', headers={
            'Authorization': 'Bearer your_api_token'
        })
        if response.status_code == 200:
            data = response.json()
            # Process and update the portal database with the data
            sync_record.last_synced = datetime.utcnow()
            CoreBankingSyncRepository.update(sync_record)
        else:
            raise Exception('Error synchronizing data with core banking system')

    @staticmethod
    def get_sync_status(entity: str) -> CoreBankingSync:
        return CoreBankingSyncRepository.find_by_entity(entity)

    @staticmethod
    def get_all_sync_statuses() -> list[CoreBankingSync]:
        return CoreBankingSyncRepository.find_all()


# File 4: Core Banking Data Sync Controller in `controllers/integration/core_banking_sync_controller.py`