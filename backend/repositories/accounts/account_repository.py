# Epic Title: Account Opening and Service Modifications

from backend.models.accounts.account_model import Account
from backend.app import db

class AccountRepository:
    @staticmethod
    def get_accounts_by_user(user_id: int) -> list[Account]:
        return Account.query.filter_by(user_id=user_id).all()

    @staticmethod
    def save(account: Account) -> None:
        db.session.add(account)
        db.session.commit()

    @staticmethod
    def create_account(user_id: int, account_number: str, account_type: str, balance: int) -> Account:
        new_account = Account(user_id=user_id, account_number=account_number, account_type=account_type, balance=balance)
        AccountRepository.save(new_account)
        return new_account


# File 4: Service Layer for Account Opening in services/account/opening/account_opening_service.py