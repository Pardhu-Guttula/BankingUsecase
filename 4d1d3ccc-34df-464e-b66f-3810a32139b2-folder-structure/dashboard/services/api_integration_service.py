# Epic Title: Core Banking System Integration

import requests
from requests.auth import HTTPBasicAuth
from typing import Any, Dict

class APIIntegrationService:
    @staticmethod
    def secure_post(url: str, data: Dict[str, Any], headers: Dict[str, str] = None) -> requests.Response:
        core_banking_api_url = "https://api.corebanking.com"
        username = "your_api_username"
        password = "your_api_password"
        full_url = f"{core_banking_api_url}/{url}"
        
        try:
            response = requests.post(
                full_url,
                json=data,
                headers=headers,
                auth=HTTPBasicAuth(username, password),
                timeout=30
            )
            response.raise_for_status()
            return response
        except requests.exceptions.RequestException as e:
            print(f"Error during API call: {e}")
            raise

    @staticmethod
    def secure_get(url: str, headers: Dict[str, str] = None) -> requests.Response:
        core_banking_api_url = "https://api.corebanking.com"
        username = "your_api_username"
        password = "your_api_password"
        full_url = f"{core_banking_api_url}/{url}"

        try:
            response = requests.get(
                full_url,
                headers=headers,
                auth=HTTPBasicAuth(username, password),
                timeout=30
            )
            response.raise_for_status()
            return response
        except requests.exceptions.RequestException as e:
            print(f"Error during API call: {e}")
            raise


# File 2: API Controller for Endpoint to Manage Secure API Calls in dashboard/controllers/api_controller.py