# Epic Title: Core Banking System Integration

from backend.models.core_banking.integration_settings_model import IntegrationSettings
from backend.app import db

class IntegrationSettingsRepository:
    @staticmethod
    def save(settings: IntegrationSettings) -> None:
        db.session.add(settings)
        db.session.commit()

    @staticmethod
    def get_settings() -> IntegrationSettings:
        return IntegrationSettings.query.first()

    @staticmethod
    def update_settings(settings: IntegrationSettings) -> None:
        existing_settings = IntegrationSettingsRepository.get_settings()
        if existing_settings:
            existing_settings.core_banking_api_url = settings.core_banking_api_url
            existing_settings.core_banking_api_key = settings.core_banking_api_key
            existing_settings.last_updated = settings.last_updated
            db.session.commit()
        else:
            IntegrationSettingsRepository.save(settings)


# File 3: Integration Service to Handle Core Banking Data in integration/services/integration_service.py