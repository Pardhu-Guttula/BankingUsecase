# Epic Title: Core Banking System Integration

from backend.integration.repositories.sync_record_repository import SyncRecordRepository
import datetime

class SyncService:
    @staticmethod
    def sync_data(entity: str, data: dict) -> bool:
        try:
            # Processing synchronization logic
            # This is where the data syncing with core banking system happens.
            # For example, making external API calls or updating databases.

            # Update sync record after synchronization
            SyncRecordRepository.update_last_sync_time(entity, datetime.datetime.utcnow())
            return True
        except Exception as e:
            # Log error
            return False

    @staticmethod
    def get_last_sync_time(entity: str) -> datetime.datetime:
        sync_record = SyncRecordRepository.get_last_sync_time(entity)
        return sync_record.last_sync_time if sync_record else None


# File 4: Core Banking Synchronization Controller to Expose Sync Endpoints in integration/controllers/sync_controller.py