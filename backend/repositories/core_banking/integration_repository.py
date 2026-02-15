# Epic Title: Core Banking System Integration

from backend.models.core_banking.integration_model import CoreBankingIntegration
from backend.app import core_banking_db as db

class IntegrationRepository:
    @staticmethod
    def save(integration: CoreBankingIntegration) -> None:
        db.session.add(integration)
        db.session.commit()

    @staticmethod
    def find_by_service_name(service_name: str) -> CoreBankingIntegration:
        return CoreBankingIntegration.query.filter_by(service_name=service_name).first()

    @staticmethod
    def find_all() -> list[CoreBankingIntegration]:
        return CoreBankingIntegration.query.all()


# File 4: Sync Log Model and Repository with Portal DB Bind in models/core_banking/sync_log_model.py and repositories/core_banking/sync_log_repository.py