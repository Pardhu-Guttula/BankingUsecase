# Epic Title: Develop a User-Friendly Dashboard

from dashboard.models.account_model import Account
from backend.app import db

class AccountRepository:
    @staticmethod
    def get_accounts_by_user_id(user_id: int) -> list[Account]:
        return Account.query.filter_by(user_id=user_id).all()

    @staticmethod
    def save(account: Account) -> None:
        db.session.add(account)
        db.session.commit()


# File 4: Transaction Repository for Database Operations in dashboard/repositories/transaction_repository.py