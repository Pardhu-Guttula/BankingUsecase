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
            account = AccountRepository.get_account_by_number(account_data['account_number'])
            if account:
                account.balance = account_data['balance']
                account.last_synced = datetime.utcnow()
                AccountRepository.update(account)
            else:
                new_account = CoreBankingAccount(
                    account_number=account_data['account_number'],
                    balance=account_data['balance']
                )
                AccountRepository.save(new_account)
    
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
                new_transaction = CoreBankingTransaction(
                    account_id=account_id,
                    amount=transaction_data['amount']
                )
                TransactionRepository.save(new_transaction)


# File 6: Core Banking Sync Controller in integration/controllers/core_banking_sync_controller.py