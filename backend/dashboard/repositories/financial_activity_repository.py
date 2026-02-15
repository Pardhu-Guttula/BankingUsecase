# Epic Title: Personalized Dashboard

from backend.models.accounts.account_model import Account
from backend.app import db

class FinancialActivityRepository:
    @staticmethod
    def find_by_user_id(user_id: int) -> list[Account]:
        return Account.query.filter_by(user_id=user_id).all()


# File 6: Update Main App to Ensure Correct Initialization in app.py