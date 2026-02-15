# Epic Title: Account Opening and Service Modifications

from backend.models.account.opening_requests.account_opening_request_model import AccountOpeningRequest
from backend.app import db

class AccountOpeningRequestRepository:
    @staticmethod
    def save(request: AccountOpeningRequest) -> None:
        db.session.add(request)
        db.session.commit()

    @staticmethod
    def get_by_user_id(user_id: int) -> list[AccountOpeningRequest]:
        return AccountOpeningRequest.query.filter_by(user_id=user_id).all()

    @staticmethod
    def get_by_id(request_id: int) -> AccountOpeningRequest:
        return AccountOpeningRequest.query.filter_by(id=request_id).first()

# File 3: Account Opening Request Service in services/account/opening_requests/account_opening_request_service.py