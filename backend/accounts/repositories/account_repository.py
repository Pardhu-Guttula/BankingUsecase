# Epic Title: Develop a User-Friendly Dashboard

from backend.accounts.models.account_model import Account
from backend.app import db

class AccountRepository:
    @staticmethod
    def find_by_user_id(user_id: int) -> list[Account]:
        return Account.query.filter_by(user_id=user_id).all()


# File 4: Transaction Repository in repositories/transaction/transaction_repository.py