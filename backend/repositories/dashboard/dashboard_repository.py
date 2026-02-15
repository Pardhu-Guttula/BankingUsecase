# Epic Title: Personalized Dashboard

from backend.models.dashboard.dashboard_model import Account, Transaction
from backend.app import db

class DashboardRepository:
    @staticmethod
    def get_user_accounts(user_id: int) -> list[Account]:
        return Account.query.filter_by(user_id=user_id).all()

    @staticmethod
    def get_account_transactions(account_id: int) -> list[Transaction]:
        return Transaction.query.filter_by(account_id=account_id).all()

# File 3: Dashboard Service in services/dashboard/dashboard_service.py