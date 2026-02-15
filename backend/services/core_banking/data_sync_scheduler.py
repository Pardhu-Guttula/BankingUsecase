# Epic Title: Core Banking System Integration

import time
import threading
from backend.services.core_banking.data_sync_service import DataSyncService

class SyncScheduler:
    @staticmethod
    def start(interval: int, sync_type: str, payload: dict = None):
        def run():
            while True:
                DataSyncService.sync_data(sync_type, payload)
                time.sleep(interval)

        thread = threading.Thread(target=run)
        thread.daemon = True
        thread.start()


# File 5: Sync Log Controller to View Sync Logs in controllers/dashboard/sync_log_controller.py