# Epic Title: Core Banking System Integration

import requests
from datetime import datetime
from flask import current_app
from backend.repositories.core_banking.account_repository import AccountRepository
from backend.repositories.core_banking.transaction_repository import TransactionRepository

class CoreBankingSyncService:
    @staticmethod
    def sync_accounts():
        url = f"https://core-banking.example.com/accounts"
        headers = {
            "Authorization": f"Bearer {current_app.config['CORE_BANKING_API_TOKEN']}",
            "Content-Type": "application/json"
        }
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        accounts_data = response.json()

        for account_data in accounts_data:
            account = AccountRepository.get_account_by_id(account_data['id'])
            if account:
                account.balance = account_data['balance']
                account.last_synced = datetime.utcnow()
                AccountRepository.update(account)
            else:
                AccountRepository.save(account_data)
    
    @staticmethod
    def sync_transactions(account_id: str):
        url = f"https://core-banking.example.com/accounts/{account_id}/transactions"
        headers = {
            "Authorization": f"Bearer {current_app.config['CORE_BANKING_API_TOKEN']}",
            "Content-Type": "application/json"
        }
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        transactions_data = response.json()

        for transaction_data in transactions_data:
            transaction = TransactionRepository.get_transaction_by_id(transaction_data['id'])
            if not transaction:
                TransactionRepository.save(transaction_data)


# File 2: Core Banking Sync Controller in integration/controllers/core_banking_sync_controller.py