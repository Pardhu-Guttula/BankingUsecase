# Epic Title: Streamline Account Opening Requests

from dashboard.models.account_opening_request_model import AccountOpeningRequest
from backend.app import db

class AccountOpeningRequestRepository:
    @staticmethod
    def save(request: AccountOpeningRequest) -> None:
        db.session.add(request)
        db.session.commit()

    @staticmethod
    def get_requests_by_user_id(user_id: int) -> list[AccountOpeningRequest]:
        return AccountOpeningRequest.query.filter_by(user_id=user_id).all()


# File 3: Account Opening Service for Business Logic in dashboard/services/account_opening_service.py