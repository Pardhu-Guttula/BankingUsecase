# Epic Title: Account Opening and Service Modifications

from backend.models.account.service_modification_request_model import ServiceModificationRequest
from backend.app import db

class ServiceModificationRequestRepository:
    @staticmethod
    def save(service_modification_request: ServiceModificationRequest) -> None:
        db.session.add(service_modification_request)
        db.session.commit()

    @staticmethod
    def get_requests_by_user_id(user_id: int) -> list[ServiceModificationRequest]:
        return ServiceModificationRequest.query.filter_by(user_id=user_id).all()

    @staticmethod
    def update(service_modification_request: ServiceModificationRequest) -> None:
        db.session.commit()

    @staticmethod
    def delete(service_modification_request: ServiceModificationRequest) -> None:
        db.session.delete(service_modification_request)
        db.session.commit()

# File 3: Service Modification Request Service to Handle Business Logic in services/account/service_modification_request_service.py