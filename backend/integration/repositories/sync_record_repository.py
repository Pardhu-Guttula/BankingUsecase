# Epic Title: Core Banking System Integration

from backend.models.core_banking.sync_record_model import SyncRecord
from backend.app import db

class SyncRecordRepository:
    @staticmethod
    def save(sync_record: SyncRecord) -> None:
        db.session.add(sync_record)
        db.session.commit()

    @staticmethod
    def get_last_sync_time(entity: str) -> SyncRecord:
        return SyncRecord.query.filter_by(entity=entity).order_by(SyncRecord.last_sync_time.desc()).first()

    @staticmethod
    def update_last_sync_time(entity: str, sync_time: datetime.datetime) -> None:
        sync_record = SyncRecordRepository.get_last_sync_time(entity)
        if sync_record:
            sync_record.last_sync_time = sync_time
            db.session.commit()
        else:
            new_sync_record = SyncRecord(entity=entity, last_sync_time=sync_time)
            SyncRecordRepository.save(new_sync_record)


# File 3: Synchronization Service to Handle Business Logic for Data Sync in integration/services/sync_service.py