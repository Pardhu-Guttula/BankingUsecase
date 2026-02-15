# Epic Title: Core Banking System Integration

from backend.models.core_banking.integration_model import CoreBankingIntegration
from backend.app import db

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


# File 3: Integration Service to Handle API Calls in services/core_banking/integration_service.py