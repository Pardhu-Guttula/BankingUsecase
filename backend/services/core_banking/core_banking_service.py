# Epic Title: Core Banking System Integration

import requests
from flask import current_app

class CoreBankingService:
    @staticmethod
    def get_account_info(account_id: str) -> dict:
        url = f"https://core-banking.example.com/accounts/{account_id}"
        headers = {
            "Authorization": f"Bearer {current_app.config['CORE_BANKING_API_TOKEN']}",
            "Content-Type": "application/json"
        }
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        return response.json()

    @staticmethod
    def create_transaction(account_id: str, amount: float) -> dict:
        url = f"https://core-banking.example.com/accounts/{account_id}/transactions"
        headers = {
            "Authorization": f"Bearer {current_app.config['CORE_BANKING_API_TOKEN']}",
            "Content-Type": "application/json"
        }
        data = {
            "amount": amount
        }
        response = requests.post(url, json=data, headers=headers)
        response.raise_for_status()
        return response.json()


# File 2: Core Banking API Endpoints in integration/controllers/core_banking_api_controller.py