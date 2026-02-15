# Epic Title: Personalized Dashboard

from backend.models.dashboard.account_dashboard_model import AccountDashboard
from backend.app import db

class AccountDashboardRepository:
    @staticmethod
    def save(account_dashboard: AccountDashboard) -> None:
        db.session.add(account_dashboard)
        db.session.commit()

    @staticmethod
    def get_by_user_id(user_id: int) -> list[AccountDashboard]:
        return AccountDashboard.query.filter_by(user_id=user_id).all()

# File 3: Dashboard Service to Handle Business Logic in services/dashboard/account_dashboard_service.py