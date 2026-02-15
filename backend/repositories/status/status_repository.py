# Epic Title: Real-time Status Updates and Notifications

from backend.models.status.status_model import Status
from backend.app import db

class StatusRepository:
    @staticmethod
    def save(status: Status) -> None:
        db.session.add(status)
        db.session.commit()

    @staticmethod
    def get_status_by_request_id(request_id: int) -> list[Status]:
        return Status.query.filter_by(request_id=request_id).order_by(Status.updated_at.desc()).all()
        
    @staticmethod
    def update(status: Status) -> None:
        db.session.commit()

# File 3: Status Service to Handle Business Logic in services/status/status_service.py