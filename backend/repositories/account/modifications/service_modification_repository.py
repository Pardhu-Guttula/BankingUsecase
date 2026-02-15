# Epic Title: Account Opening and Service Modifications

from backend.models.account.modifications.service_modification_model import ServiceModificationRequest
from backend.app import db

class ServiceModificationRequestRepository:
    @staticmethod
    def save(service_modification_request: ServiceModificationRequest) -> None:
        db.session.add(service_modification_request)
        db.session.commit()

    @staticmethod
    def get_requests_by_user(user_id: int) -> list[ServiceModificationRequest]:
        return ServiceModificationRequest.query.filter_by(user_id=user_id).all()

    @staticmethod
    def get_request_by_id(request_id: int) -> ServiceModificationRequest:
        return ServiceModificationRequest.query.get(request_id)


# File 3: Service Modification Request Service in services/account/modifications/service_modification_service.py