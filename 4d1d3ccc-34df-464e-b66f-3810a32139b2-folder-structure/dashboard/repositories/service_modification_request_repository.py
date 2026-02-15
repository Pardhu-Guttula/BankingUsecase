# Epic Title: Service Modification Requests

from dashboard.models.service_modification_request_model import ServiceModificationRequest
from backend.app import db

class ServiceModificationRequestRepository:
    @staticmethod
    def save(request: ServiceModificationRequest) -> None:
        db.session.add(request)
        db.session.commit()

    @staticmethod
    def get_requests_by_user_id(user_id: int) -> list[ServiceModificationRequest]:
        return ServiceModificationRequest.query.filter_by(user_id=user_id).all()


# File 3: Service Modification Service for Business Logic in dashboard/services/service_modification_service.py