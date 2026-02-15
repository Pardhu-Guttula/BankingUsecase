# Epic Title: Personalized Dashboard

from backend.models.accounts.account_model import Account

class AccountRepository:
    @staticmethod
    def find_by_user_id(user_id: int) -> list[Account]:
        return Account.query.filter_by(user_id=user_id).all()

    @staticmethod
    def save(account: Account) -> None:
        db.session.add(account)
        db.session.commit()


# File 5: Repository for Transaction Operations in repositories/accounts/transaction_repository.py