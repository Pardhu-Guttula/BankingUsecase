# Epic Title: Core Banking System Integration

from backend.models.integration.data_sync_model import DataSyncStatus
from backend.repositories.integration.data_sync_repository import DataSyncRepository
from requests import get, post
from datetime import datetime


class DataSyncService:
    CORE_BANKING_API = 'https://api.corebanking.example.com/sync'

    @staticmethod
    def sync_data(entity: str) -> DataSyncStatus:
        last_sync = DataSyncRepository.get_last_sync_status(entity)
        params = {'last_synced_at': last_sync.last_synced_at.isoformat()} if last_sync else {}

        response = get(f"{DataSyncService.CORE_BANKING_API}/{entity}", params=params)

        if response.status_code == 200:
            data_sync_status = DataSyncStatus(entity=entity, last_synced_at=datetime.utcnow(), status='success', is_success=True)
        else:
            data_sync_status = DataSyncStatus(entity=entity, last_synced_at=datetime.utcnow(), status='failed', is_success=False)

        DataSyncRepository.save(data_sync_status)
        return data_sync_status


# File 4: Core Banking Sync API Controller in integration/controllers/core_banking_sync_controller.py