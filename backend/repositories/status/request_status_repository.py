# Epic Title: Real-time Status Updates and Notifications

from backend.models.status.request_status_model import RequestStatus
from backend.app import db

class RequestStatusRepository:
    @staticmethod
    def save(status: RequestStatus) -> None:
        db.session.add(status)
        db.session.commit()

    @staticmethod
    def get_by_request_id(request_id: int) -> RequestStatus:
        return RequestStatus.query.filter_by(request_id=request_id).first()

    @staticmethod
    def get_by_user_id(user_id: int) -> list[RequestStatus]:
        return RequestStatus.query.filter_by(user_id=user_id).all()

# File 3: Request Status Service in services/status/request_status_service.py