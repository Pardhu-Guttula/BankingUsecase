# Epic Title: Core Banking System Integration

from backend.integration.repositories.integration_settings_repository import IntegrationSettingsRepository
from backend.models.core_banking.integration_settings_model import IntegrationSettings
import requests
import json

class IntegrationService:
    @staticmethod
    def fetch_core_banking_data(endpoint: str, params: dict) -> dict:
        settings: IntegrationSettings = IntegrationSettingsRepository.get_settings()
        response = requests.get(
            url=f"{settings.core_banking_api_url}/{endpoint}",
            headers={"Authorization": f"Bearer {settings.core_banking_api_key}"},
            params=params
        )
        if response.status_code == 200:
            return json.loads(response.text)
        else:
            # Handle error scenarios, maybe log the issue
            return {}


# File 4: Integration Controller for Endpoint Exposure in integration/controllers/integration_controller.py