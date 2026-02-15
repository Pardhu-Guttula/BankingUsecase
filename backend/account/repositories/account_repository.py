# Epic Title: Account Opening and Service Modifications

from backend.models.accounts.account_model import Account
from backend.app import db

class AccountRepository:
    @staticmethod
    def save(account: Account) -> None:
        db.session.add(account)
        db.session.commit()

    @staticmethod
    def find_by_user_id(user_id: int) -> list[Account]:
        return Account.query.filter_by(user_id=user_id).all()


# File 5: Account Opening Template for User Interface in templates/open_account.html