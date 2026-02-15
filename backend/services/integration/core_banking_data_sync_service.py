# Epic Title: Core Banking System Integration

from backend.models.integration.core_banking_data_model import CoreBankingData
from backend.repositories.integration.core_banking_data_repository import CoreBankingDataRepository
from backend.repositories.integration.data_sync_repository import DataSyncRepository
from backend.models.integration.data_sync_model import DataSyncStatus
from requests import get, post
from datetime import datetime
import json


class CoreBankingDataSyncService:
    CORE_BANKING_API = 'https://api.corebanking.example.com/sync'

    @staticmethod
    def sync_data(entity: str) -> DataSyncStatus:
        last_sync = DataSyncRepository.get_last_sync_status(entity)
        params = {'last_synced_at': last_sync.last_synced_at.isoformat()} if last_sync else {}

        response = get(f"{CoreBankingDataSyncService.CORE_BANKING_API}/{entity}", params=params)

        if response.status_code == 200:
            fetched_data = response.json()
            for data in fetched_data:
                entity_id = data.pop('entity_id')
                core_banking_data = CoreBankingDataRepository.get_data_by_entity(entity_id, entity)
                if core_banking_data:
                    core_banking_data.data = json.dumps(data)
                    core_banking_data.updated_at = datetime.utcnow()
                    CoreBankingDataRepository.update_data(core_banking_data)
                else:
                    core_banking_data = CoreBankingData(entity_id=entity_id, entity_type=entity, data=json.dumps(data))
                    CoreBankingDataRepository.save(core_banking_data)
            
            data_sync_status = DataSyncStatus(entity=entity, last_synced_at=datetime.utcnow(), status='success', is_success=True)
        else:
            data_sync_status = DataSyncStatus(entity=entity, last_synced_at=datetime.utcnow(), status='failed', is_success=False)

        DataSyncRepository.save(data_sync_status)
        return data_sync_status


# File 4: Core Banking Data API Controller in integration/controllers/core_banking_data_controller.py