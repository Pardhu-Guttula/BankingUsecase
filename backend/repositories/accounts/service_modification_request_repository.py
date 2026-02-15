# Epic Title: Account Opening and Service Modifications

from backend.models.accounts.service_modification_request_model import ServiceModificationRequest

class ServiceModificationRequestRepository:
    @staticmethod
    def save(request: ServiceModificationRequest) -> None:
        db.session.add(request)
        db.session.commit()

    @staticmethod
    def find_by_user_id(user_id: int) -> list[ServiceModificationRequest]:
        return ServiceModificationRequest.query.filter_by(user_id=user_id).all()

    @staticmethod
    def update(request: ServiceModificationRequest) -> None:
        db.session.commit()


# File 4: Account Service Update to Handle Service Modification Requests in services/accounts/account_service.py