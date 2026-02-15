# Epic Title: Real-time Status Updates and Notifications

from backend.models.status.status_model import Status
from backend.app import db

class StatusRepository:
    @staticmethod
    def save(status: Status) -> None:
        db.session.add(status)
        db.session.commit()

    @staticmethod
    def update(status: Status) -> None:
        db.session.commit()

    @staticmethod
    def find_by_request_id(request_id: int) -> list[Status]:
        return Status.query.filter_by(request_id=request_id).all()


# File 3: Status Service to Handle Business Logic for Real-Time Updates in status/services/status_service.py