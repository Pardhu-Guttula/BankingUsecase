# Epic Title: Core Banking System Integration

import requests
from backend.repositories.core_banking.integration_repository import IntegrationRepository
from backend.models.core_banking.sync_log_model import SyncLog
from backend.repositories.core_banking.sync_log_repository import SyncLogRepository

class DataSyncService:
    @staticmethod
    def sync_data(sync_type: str, payload: dict = None) -> None:
        try:
            integration = IntegrationRepository.find_by_service_name(sync_type)
            if not integration:
                raise ValueError("Integration service not found for sync type")

            url = integration.endpoint
            headers = {"Content-Type": "application/json"}

            if integration.request_type.lower() == "post":
                response = requests.post(url, json=payload, headers=headers)
            elif integration.request_type.lower() == "get":
                response = requests.get(url, params=payload, headers=headers)
            else:
                raise ValueError("Unsupported request type")

            if response.status_code == 200:
                sync_log = SyncLog(sync_type, "success", "Data synchronized successfully")
            else:
                sync_log = SyncLog(sync_type, "failure", f"Error: {response.text}")
        except Exception as e:
            sync_log = SyncLog(sync_type, "error", str(e))

        SyncLogRepository.save(sync_log)


# File 4: Scheduler to Trigger Data Sync at Intervals in services/core_banking/data_sync_scheduler.py