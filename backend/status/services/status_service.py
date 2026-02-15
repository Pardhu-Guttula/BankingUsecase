# Epic Title: Real-time Status Updates and Notifications

from backend.models.status.status_model import Status
from backend.status.repositories.status_repository import StatusRepository
from backend.notifications.services.notification_service import NotificationService
from backend.app import db

class StatusService:
    @staticmethod
    def create_status(request_id: int, status: str, user_id: int) -> bool:
        try:
            new_status = Status(request_id=request_id, status=status)
            StatusRepository.save(new_status)
            NotificationService.create_notification(user_id, f"Your request has a new status: {status}")
            return True
        except Exception as e:
            db.session.rollback()
            return False

    @staticmethod
    def update_status(status_id: int, new_status: str, user_id: int) -> bool:
        try:
            status = Status.query.get(status_id)
            if status:
                status.status = new_status
                status.updated_at = db.func.now()
                StatusRepository.update(status)
                NotificationService.create_notification(user_id, f"Your request status has been updated to: {new_status}")
                return True
            return False
        except Exception as e:
            db.session.rollback()
            return False


# File 6: Update Status Controller to Include User ID in status/controllers/status_controller.py