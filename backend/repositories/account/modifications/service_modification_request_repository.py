# Epic Title: Account Opening and Service Modifications

from backend.models.account.modifications.service_modification_request_model import ServiceModificationRequest
from backend.app import db

class ServiceModificationRequestRepository:
    @staticmethod
    def save(request: ServiceModificationRequest) -> None:
        db.session.add(request)
        db.session.commit()

    @staticmethod
    def get_by_user_id(user_id: int) -> list[ServiceModificationRequest]:
        return ServiceModificationRequest.query.filter_by(user_id=user_id).all()

    @staticmethod
    def get_by_account_id(account_id: int) -> list[ServiceModificationRequest]:
        return ServiceModificationRequest.query.filter_by(account_id=account_id).all()

    @staticmethod
    def get_by_id(request_id: int) -> ServiceModificationRequest:
        return ServiceModificationRequest.query.filter_by(id=request_id).first()

# File 3: Service Modification Request Service in services/account/modifications/service_modification_request_service.py