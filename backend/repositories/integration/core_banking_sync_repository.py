# Epic Title: Data Synchronization Mechanisms

from backend.models.integration.core_banking_sync_model import CoreBankingSync
from backend.app import db

class CoreBankingSyncRepository:
    @staticmethod
    def save(sync_record: CoreBankingSync) -> None:
        db.session.add(sync_record)
        db.session.commit()

    @staticmethod
    def update(sync_record: CoreBankingSync) -> None:
        db.session.commit()

    @staticmethod
    def find_by_entity(entity: str) -> CoreBankingSync:
        return CoreBankingSync.query.filter_by(entity=entity).first()

    @staticmethod
    def find_all() -> list[CoreBankingSync]:
        return CoreBankingSync.query.all()


# File 3: Core Banking Data Sync Service in `services/integration/core_banking_sync_service.py`