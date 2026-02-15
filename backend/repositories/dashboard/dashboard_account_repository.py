# Epic Title: Personalized Dashboard

from backend.models.dashboard.dashboard_account_model import DashboardAccount
from backend.app import db


class DashboardAccountRepository:
    @staticmethod
    def save(dashboard_account: DashboardAccount) -> None:
        db.session.add(dashboard_account)
        db.session.commit()

    @staticmethod
    def get_accounts_by_user_id(user_id: int) -> list[DashboardAccount]:
        return DashboardAccount.query.filter_by(user_id=user_id).all()

    @staticmethod
    def update(dashboard_account: DashboardAccount) -> None:
        db.session.commit()

    @staticmethod
    def delete(dashboard_account: DashboardAccount) -> None:
        db.session.delete(dashboard_account)
        db.session.commit()


# File 3: Dashboard Account Service to Handle Business Logic in services/dashboard/dashboard_account_service.py