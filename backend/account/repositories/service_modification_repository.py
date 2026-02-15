# Epic Title: Account Opening and Service Modifications

from backend.models.accounts.service_modification_request import ServiceModificationRequest
from backend.app import db

class ServiceModificationRepository:
    @staticmethod
    def save(modification_request: ServiceModificationRequest) -> None:
        db.session.add(modification_request)
        db.session.commit()

    @staticmethod
    def find_by_user_id(user_id: int) -> list[ServiceModificationRequest]:
        return ServiceModificationRequest.query.filter_by(user_id=user_id).all()


# File 5: Service Modification Request Model to Define Modification Requests in models/accounts/service_modification_request.py