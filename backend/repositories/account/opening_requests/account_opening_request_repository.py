# Epic Title: Streamline Account Opening Requests

from backend.models.account.opening_requests.account_opening_request_model import AccountOpeningRequest
from backend.app import db

class AccountOpeningRequestRepository:
    @staticmethod
    def save(request: AccountOpeningRequest) -> None:
        db.session.add(request)
        db.session.commit()

    @staticmethod
    def find_by_user_id(user_id: int) -> list[AccountOpeningRequest]:
        return AccountOpeningRequest.query.filter_by(user_id=user_id).all()


# File 3: Account Opening Request Service in services/account/opening_requests/account_opening_request_service.py