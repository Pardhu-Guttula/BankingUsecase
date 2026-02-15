# Epic Title: Maintain Separate Database

from core_integration.models import core_banking_db as db

# Define Core Banking DB models here

class CoreBankingAccount(db.Model):
    __tablename__ = 'core_banking_accounts'

    id = db.Column(db.Integer, primary_key=True)
    account_number = db.Column(db.String(20), unique=True, nullable=False)
    balance = db.Column(db.Float, nullable=False)
    user_id = db.Column(db.Integer, nullable=False)
    created_at = db.Column(db.DateTime, nullable=False)

    def __init__(self, account_number: str, balance: float, user_id: int):
        self.account_number = account_number
        self.balance = balance
        self.user_id = user_id


# File 6: requirements.txt Update