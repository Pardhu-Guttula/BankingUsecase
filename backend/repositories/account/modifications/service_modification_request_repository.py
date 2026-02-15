# Epic Title: Service Modification Requests

from backend.models.account.modifications.service_modification_request_model import ServiceModificationRequest
from backend.app import db

class ServiceModificationRequestRepository:
    @staticmethod
    def save(request: ServiceModificationRequest) -> None:
        db.session.add(request)
        db.session.commit()

    @staticmethod
    def find_by_user_id(user_id: int) -> list[ServiceModificationRequest]:
        return ServiceModificationRequest.query.filter_by(user_id=user_id).all()


# File 3: Service Modification Request Service in services/account/modifications/service_modification_request_service.py