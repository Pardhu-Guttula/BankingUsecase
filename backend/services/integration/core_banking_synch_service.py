# Epic Title: Core Banking System Integration

import requests
from requests.auth import HTTPBasicAuth
import os
from backend.repositories.integration.integration_repository import CoreBankingDataRepository
from backend.models.integration.core_banking_data_model import CoreBankingData

class CoreBankingSyncService:
    BASE_URL = os.getenv("CORE_BANKING_API_BASE_URL", "https://corebanking.example.com/api")
    USERNAME = os.getenv("CORE_BANKING_API_USERNAME", "apiuser")
    PASSWORD = os.getenv("CORE_BANKING_API_PASSWORD", "apipassword")

    @staticmethod
    def fetch_core_data(endpoint: str) -> list[dict]:
        url = f"{CoreBankingSyncService.BASE_URL}/{endpoint}"
        response = requests.get(url, auth=HTTPBasicAuth(CoreBankingSyncService.USERNAME, CoreBankingSyncService.PASSWORD))
        response.raise_for_status()
        return response.json()

    @staticmethod
    def sync_data(endpoint: str) -> None:
        data = CoreBankingSyncService.fetch_core_data(endpoint)
        CoreBankingDataRepository.save_data(data)

# File 3: Integration Core Banking Model in models/integration/core_banking_data_model.py