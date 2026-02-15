# Epic Title: Core Banking System Integration

import requests
from backend.repositories.core_banking.integration_repository import IntegrationRepository
from backend.models.core_banking.integration_model import CoreBankingIntegration

class IntegrationService:
    @staticmethod
    def call_core_banking_api(service_name: str, payload: dict) -> dict:
        integration = IntegrationRepository.find_by_service_name(service_name)
        if not integration:
            raise ValueError("Service not found")

        url = integration.endpoint
        headers = {"Content-Type": "application/json"}

        if integration.request_type.lower() == "post":
            response = requests.post(url, json=payload, headers=headers)
        elif integration.request_type.lower() == "get":
            response = requests.get(url, params=payload, headers=headers)
        else:
            raise ValueError("Unsupported request type")

        if response.status_code != 200:
            raise Exception("API call failed")

        return response.json()


# File 4: Secure API Controller to Manage Requests in controllers/dashboard/secure_api_controller.py