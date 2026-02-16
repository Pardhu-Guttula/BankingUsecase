# Epic Title: Develop a User-Friendly Dashboard

import logging
from typing import List
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