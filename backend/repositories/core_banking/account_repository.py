# Epic Title: Core Banking System Integration

from backend.models.core_banking.account_model import CoreBankingAccount
from backend.app import db

class AccountRepository:
    @staticmethod
    def get_account_by_id(account_id: int) -> CoreBankingAccount:
        return CoreBankingAccount.query.get(account_id)

    @staticmethod
    def get_account_by_number(account_number: str) -> CoreBankingAccount:
        return CoreBankingAccount.query.filter_by(account_number=account_number).first()

    @staticmethod
    def save(account: CoreBankingAccount) -> None:
        db.session.add(account)
        db.session.commit()

    @staticmethod
    def update(account: CoreBankingAccount) -> None:
        db.session.commit()


# File 4: Core Banking Transaction Repository in repositories/core_banking/transaction_repository.py