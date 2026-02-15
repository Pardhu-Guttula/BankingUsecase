# Epic Title: Real-time Status Updates and Notifications

from backend.models.status.status_model import Status
from backend.status.repositories.status_repository import StatusRepository
from backend.app import db

class StatusService:
    @staticmethod
    def create_status(request_id: int, status: str) -> bool:
        try:
            new_status = Status(request_id=request_id, status=status)
            StatusRepository.save(new_status)
            return True
        except Exception as e:
            db.session.rollback()
            return False

    @staticmethod
    def update_status(status_id: int, new_status: str) -> bool:
        try:
            status = Status.query.get(status_id)
            if status:
                status.status = new_status
                status.updated_at = db.func.now()
                StatusRepository.update(status)
                return True
            return False
        except Exception as e:
            db.session.rollback()
            return False


# File 4: Status Controller to Manage Real-Time Status API Endpoints in status/controllers/status_controller.py