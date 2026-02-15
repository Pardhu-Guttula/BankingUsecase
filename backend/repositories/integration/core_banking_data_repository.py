# Epic Title: Core Banking System Integration

from backend.models.integration.core_banking_data_model import CoreBankingData
from backend.app import db


class CoreBankingDataRepository:
    @staticmethod
    def save(core_banking_data: CoreBankingData) -> None:
        db.session.add(core_banking_data)
        db.session.commit()

    @staticmethod
    def get_data_by_entity(entity_id: int, entity_type: str) -> CoreBankingData:
        return CoreBankingData.query.filter_by(entity_id=entity_id, entity_type=entity_type).first()

    @staticmethod
    def update_data(core_banking_data: CoreBankingData) -> None:
        db.session.commit()


# File 3: Core Banking Data Sync Service to Integrate with Core Banking System in services/integration/core_banking_data_sync_service.py