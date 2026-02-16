# Epic Title: Overview of Financial Activities

import logging
from typing import List, Dict, Any
from backend.dashboard.models.account import Account
from backend.dashboard.models.transaction import Transaction

logger = logging.getLogger(__name__)

class DashboardService:
    def __init__(self, db):
        self.db = db
    
    def get_accounts_by_user_id(self, user_id: int) -> List[Account]:
        accounts = Account.query.filter_by(user_id=user_id).all()
        logger.info(f"Retrieved {len(accounts)} accounts for user_id: {user_id}")
        return accounts

    def get_transactions_by_account_id(self, account_id: int) -> List[Transaction]:
        transactions = Transaction.query.filter_by(account_id=account_id).all()
        logger.info(f"Retrieved {len(transactions)} transactions for account_id: {account_id}")
        return transactions
    
    def get_financial_summary(self, user_id: int) -> Dict[str, Any]:
        accounts = self.get_accounts_by_user_id(user_id)
        total_balance = sum(account.balance for account in accounts)
        
        transactions_data = []
        for account in accounts:
            transactions = self.get_transactions_by_account_id(account.id)
            account_data = {
                "account_number": account.account_number,
                "account_type": account.account_type,
                "balance": account.balance,
                "transactions": [
                    {
                        "amount": transaction.amount,
                        "transaction_type": transaction.transaction_type,
                        "description": transaction.description,
                        "created_at": transaction.created_at
                    }
                    for transaction in transactions
                ]
            }
            transactions_data.append(account_data)
        
        summary = {
            "total_balance": total_balance,
            "accounts_data": transactions_data
        }
        
        logger.info(f"Generated financial summary for user_id: {user_id}")
        return summary