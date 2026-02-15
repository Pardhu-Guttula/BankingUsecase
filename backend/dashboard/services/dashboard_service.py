# Epic Title: Develop a User-Friendly Dashboard

from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
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



# File 7: Database Schema for UserProfile in database/user_profiles.sql