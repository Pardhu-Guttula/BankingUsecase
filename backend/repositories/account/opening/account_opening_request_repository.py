# Epic Title: Account Opening and Service Modifications

from backend.models.account.opening.account_opening_request_model import AccountOpeningRequest
from backend.app import db

class AccountOpeningRequestRepository:
    @staticmethod
    def save(account_opening_request: AccountOpeningRequest) -> None:
        db.session.add(account_opening_request)
        db.session.commit()

    @staticmethod
    def get_requests_by_user(user_id: int) -> list[AccountOpeningRequest]:
        return AccountOpeningRequest.query.filter_by(user_id=user_id).all()

    @staticmethod
    def get_request_by_id(request_id: int) -> AccountOpeningRequest:
        return AccountOpeningRequest.query.get(request_id)


# File 3: Account Opening Service in services/account/opening/account_opening_request_service.py