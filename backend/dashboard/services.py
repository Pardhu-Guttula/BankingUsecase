# Epic Title: Personalized Dashboard

import logging
from flask_sqlalchemy import SQLAlchemy
from backend.dashboard.models import Account, Transaction, Widget
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

    def get_user_widgets(self, user_id: int) -> list[Widget]:
        logger.debug(f"Fetching widgets for user {user_id}")
        return Widget.query.filter_by(user_id=user_id).all()

    def get_dashboard_data(self, user_id: int) -> dict:
        logger.debug(f"Fetching dashboard data for user {user_id}")
        accounts = self.get_user_accounts(user_id)
        widgets = self.get_user_widgets(user_id)
        result = {
            "accounts": [account for account in accounts],
            "widgets": [widget for widget in widgets]
        }
        for account in accounts:
            transactions = self.get_account_transactions(account.id)
            result[account.account_number] = transactions
        return result

    def add_widget_for_user(self, user_id: int, widget_name: str, config: str) -> Widget:
        widget = Widget(user_id=user_id, name=widget_name, config=config)
        self.db.session.add(widget)
        self.db.session.commit()
        logger.debug(f"Added widget {widget_name} for user {user_id}")
        return widget

    def remove_widget_for_user(self, user_id: int, widget_id: int):
        widget = Widget.query.filter_by(user_id=user_id, id=widget_id).first()
        if widget:
            self.db.session.delete(widget)
            self.db.session.commit()
            logger.debug(f"Removed widget {widget_id} for user {user_id}")
        else:
            logger.warn(f"Widget {widget_id} not found for user {user_id}")
            
    def get_financial_summary(self, user_id: int) -> dict:
        accounts = self.get_user_accounts(user_id)
        summary = {
            "total_balance": sum(account.balance for account in accounts),
            "total_transactions": 0,
            "recent_transactions": []
        }

        for account in accounts:
            transactions = self.get_account_transactions(account.id, limit=5)
            summary["total_transactions"] += len(transactions)
            summary["recent_transactions"].extend(transactions)

        summary["recent_transactions"] = sorted(
            summary["recent_transactions"], key=lambda x: x.timestamp, reverse=True)[:5]
        
        logger.debug(f"Financial summary for user {user_id}: {summary}")
        return summary