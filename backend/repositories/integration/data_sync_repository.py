# Epic Title: Core Banking System Integration

from backend.models.integration.data_sync_model import DataSyncStatus
from backend.app import db


class DataSyncRepository:
    @staticmethod
    def save(data_sync_status: DataSyncStatus) -> None:
        db.session.add(data_sync_status)
        db.session.commit()

    @staticmethod
    def get_last_sync_status(entity: str) -> DataSyncStatus:
        return DataSyncStatus.query.filter_by(entity=entity).order_by(DataSyncStatus.last_synced_at.desc()).first()

    @staticmethod
    def update(data_sync_status: DataSyncStatus) -> None:
        db.session.commit()


# File 3: Data Sync Service to Integrate with Core Banking System in services/integration/data_sync_service.py