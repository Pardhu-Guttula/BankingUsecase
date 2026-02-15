# Epic Title: Real-time Status Updates and Notifications

from dashboard.models.status_update_model import StatusUpdate
from backend.app import db

class StatusUpdateRepository:
    @staticmethod
    def save(status_update: StatusUpdate) -> None:
        db.session.add(status_update)
        db.session.commit()

    @staticmethod
    def get_updates_by_request_id(request_id: int) -> list[StatusUpdate]:
        return StatusUpdate.query.filter_by(request_id=request_id).all()


# File 3: Status Update Service for Business Logic in dashboard/services/status_update_service.py