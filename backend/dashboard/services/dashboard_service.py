# Epic Title: Overview of Financial Activities

from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine, func
from ..models.user_profile import UserProfile
from account.models.account import Account
from account.models.transaction import Transaction

DATABASE_URI = 'mysql+pymysql://username:password@localhost/db_name'
engine = create_engine(DATABASE_URI)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

class DashboardService:
    def __init__(self):
        self.db = SessionLocal()

    def get_user_profile(self, user_id: int):
        return self.db.query(UserProfile).filter(UserProfile.user_id == user_id).first()

    def get_user_accounts(self, user_id: int):
        return self.db.query(Account).filter(Account.user_id == user_id).all()

    def get_user_transactions(self, user_id: int):
        accounts = self.get_user_accounts(user_id)
        account_ids = [account.id for account in accounts]
        return self.db.query(Transaction).filter(Transaction.account_id.in_(account_ids)).all()

    def get_financial_summary(self, user_id: int):
        accounts = self.get_user_accounts(user_id)
        total_balance = sum(account.balance for account in accounts)
        transactions = self.get_user_transactions(user_id)

        total_credits = sum(transaction.amount for transaction in transactions if transaction.transaction_type == 'credit')
        total_debits = sum(transaction.amount for transaction in transactions if transaction.transaction_type == 'debit')

        summary = {
            'total_balance': total_balance,
            'total_credits': total_credits,
            'total_debits': total_debits
        }

        return summary



# File 3: app.py Update for Financial Summary