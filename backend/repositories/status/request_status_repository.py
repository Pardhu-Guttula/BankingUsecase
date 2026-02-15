# Epic Title: Real-time Status Updates

from backend.models.status.request_status_model import RequestStatus
from backend.app import db

class RequestStatusRepository:
    @staticmethod
    def save(status: RequestStatus) -> None:
        db.session.add(status)
        db.session.commit()

    @staticmethod
    def update(status: RequestStatus) -> None:
        db.session.commit()

    @staticmethod
    def find_by_request_id(request_id: int) -> list[RequestStatus]:
        return RequestStatus.query.filter_by(request_id=request_id).order_by(RequestStatus.updated_at).all()


# File 3: Status Update Service in services/status/request_status_service.py