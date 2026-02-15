# Epic Title: Account Opening and Service Modifications

from backend.models.account.opening_request_model import OpeningRequest
from backend.app import db

class OpeningRequestRepository:
    @staticmethod
    def save(opening_request: OpeningRequest) -> None:
        db.session.add(opening_request)
        db.session.commit()

    @staticmethod
    def get_requests_by_user_id(user_id: int) -> list[OpeningRequest]:
        return OpeningRequest.query.filter_by(user_id=user_id).all()

    @staticmethod
    def update(opening_request: OpeningRequest) -> None:
        db.session.commit()

    @staticmethod
    def delete(opening_request: OpeningRequest) -> None:
        db.session.delete(opening_request)
        db.session.commit()

# File 3: Account Opening Request Service to Handle Business Logic in services/account/opening_request_service.py