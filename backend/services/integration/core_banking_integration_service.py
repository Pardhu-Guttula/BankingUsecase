# Epic Title: Core Banking System Integration

import requests
from requests.auth import HTTPBasicAuth
import os

class CoreBankingIntegrationService:
    BASE_URL = os.getenv("CORE_BANKING_API_BASE_URL", "https://corebanking.example.com/api")
    USERNAME = os.getenv("CORE_BANKING_API_USERNAME", "apiuser")
    PASSWORD = os.getenv("CORE_BANKING_API_PASSWORD", "apipassword")

    @staticmethod
    def secure_get(endpoint: str, params: dict = None) -> dict:
        url = f"{CoreBankingIntegrationService.BASE_URL}/{endpoint}"
        response = requests.get(url, params=params, auth=HTTPBasicAuth(CoreBankingIntegrationService.USERNAME, CoreBankingIntegrationService.PASSWORD))
        response.raise_for_status()
        return response.json()

    @staticmethod
    def secure_post(endpoint: str, data: dict) -> dict:
        url = f"{CoreBankingIntegrationService.BASE_URL}/{endpoint}"
        response = requests.post(url, json=data, auth=HTTPBasicAuth(CoreBankingIntegrationService.USERNAME, CoreBankingIntegrationService.PASSWORD))
        response.raise_for_status()
        return response.json()

# File 2: Core Banking API Controller in integration/controllers/core_banking_api_controller.py