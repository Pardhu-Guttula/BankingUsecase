# Epic Title: Core Banking System Integration

from backend.models.core_banking.sync_log_model import SyncLog
from backend.app import db

class SyncLogRepository:
    @staticmethod
    def save(sync_log: SyncLog) -> None:
        db.session.add(sync_log)
        db.session.commit()

    @staticmethod
    def find_all() -> list[SyncLog]:
        return SyncLog.query.all()


# File 3: Data Sync Service to Handle Sync Mechanisms in services/core_banking/data_sync_service.py