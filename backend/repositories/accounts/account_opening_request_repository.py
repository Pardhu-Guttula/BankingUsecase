# Epic Title: Account Opening and Service Modifications

from backend.models.accounts.account_opening_request_model import AccountOpeningRequest

class AccountOpeningRequestRepository:
    @staticmethod
    def save(request: AccountOpeningRequest) -> None:
        db.session.add(request)
        db.session.commit()

    @staticmethod
    def find_by_user_id(user_id: int) -> list[AccountOpeningRequest]:
        return AccountOpeningRequest.query.filter_by(user_id=user_id).all()


# File 4: Account Service Update to Handle Account Opening Requests in services/accounts/account_service.py