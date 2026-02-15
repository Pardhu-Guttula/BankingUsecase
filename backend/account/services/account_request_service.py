# Epic Title: Streamline Account Opening Requests

from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from ..models.account_request import AccountRequest

DATABASE_URI = 'mysql+pymysql://username:password@localhost/db_name'
engine = create_engine(DATABASE_URI)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

class AccountRequestService:
    def __init__(self):
        self.db = SessionLocal()

    def create_account_request(self, user_id: int, account_type: str) -> bool:
        new_request = AccountRequest(user_id=user_id, account_type=account_type)
        self.db.add(new_request)
        self.db.commit()
        return True

    def get_account_requests(self, user_id: int):
        requests = self.db.query(AccountRequest).filter(AccountRequest.user_id == user_id).all()
        return [{'id': request.id, 'account_type': request.account_type, 'status': request.status} for request in requests]



# File 5: Database Schema for AccountRequest in database/account_requests.sql