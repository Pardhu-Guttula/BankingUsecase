# Epic Title: Real-time Status Updates and Notifications

from backend.models.status.request_status_model import RequestStatus
from backend.app import db

class RequestStatusRepository:
    @staticmethod
    def get_statuses_by_user(user_id: int) -> list[RequestStatus]:
        return RequestStatus.query.filter_by(user_id=user_id).all()

    @staticmethod
    def save(request_status: RequestStatus) -> None:
        db.session.add(request_status)
        db.session.commit()

    @staticmethod
    def update(request_status: RequestStatus) -> None:
        db.session.commit()


# File 4: Status Service Layer in services/status/request_status_service.py