# Epic Title: Personalized Dashboard

from typing import List
from backend.models.account.account_model import Account
from backend.app import db

class AccountRepository:
    @staticmethod
    def get_user_accounts(user_id: int) -> List[Account]:
        return Account.query.filter_by(user_id=user_id).all()


# File 4: Transaction Repository for Fetching User Transactions in repositories/transaction/transaction_repository.py (Existing File, Re-emitting for Context)