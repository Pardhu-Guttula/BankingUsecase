# Epic Title: Personalized Dashboard

import logging
from flask_sqlalchemy import SQLAlchemy
from backend.dashboard.models import Account, Transaction
from backend.authentication.models import User

logger = logging.getLogger(__name__)

class DashboardService:
    def __init__(self, db: SQLAlchemy):
        self.db = db

    def get_user_accounts(self, user_id: int) -> list[Account]:
        logger.debug(f"Fetching accounts for user {user_id}")
        return Account.query.filter_by(user_id=user_id).all()

    def get_account_transactions(self, account_id: int, limit: int = 10) -> list[Transaction]:
        logger.debug(f"Fetching transactions for account {account_id}")
        return Transaction.query.filter_by(account_id=account_id).order_by(Transaction.timestamp.desc()).limit(limit).all()

    def get_dashboard_data(self, user_id: int) -> dict:
        logger.debug(f"Fetching dashboard data for user {user_id}")
        accounts = self.get_user_accounts(user_id)
        result = []
        for account in accounts:
            transactions = self.get_account_transactions(account.id)
            result.append({
                "account": account,
                "transactions": transactions
            })
        return result