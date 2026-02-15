# Epic Title: Develop Secure APIs

import requests
from requests.auth import HTTPBasicAuth
from typing import Any, Dict

class BankingService:
    BASE_URL = "https://api.corebanking.com"
    API_USERNAME = "api_user"
    API_PASSWORD = "api_password"

    @staticmethod
    def make_secure_request(endpoint: str, method: str = "GET", data: Dict[str, Any] = None) -> Dict[str, Any]:
        url = f"{BankingService.BASE_URL}/{endpoint}"
        auth = HTTPBasicAuth(BankingService.API_USERNAME, BankingService.API_PASSWORD)
        
        headers = {
            "Content-Type": "application/json",
            "Accept": "application/json"
        }

        try:
            if method == "GET":
                response = requests.get(url, headers=headers, auth=auth)
            else:
                response = requests.post(url, headers=headers, json=data, auth=auth)
            
            response.raise_for_status()

            return response.json()
        except requests.RequestException as e:
            # Add structured logging for the exception
            print(f"Request to {url} failed: {e}")
            raise


# File 2: Core Banking API Controller in core_integration/controllers/banking_controller.py