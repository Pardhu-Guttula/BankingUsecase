# Epic Title: Real-time Status Updates and Notifications

from backend.models.status.status_model import Status
from backend.status.repositories.status_repository import StatusRepository
from backend.services.notifications.email_notification_service import EmailNotificationService
from backend.app import db

class StatusService:
    @staticmethod
    def create_status(request_id: int, status: str, user_email: str) -> bool:
        try:
            new_status = Status(request_id=request_id, status=status)
            StatusRepository.save(new_status)
            EmailNotificationService.send_notification(user_email, "New Status Update", f"Your request has a new status: {status}")
            return True
        except Exception as e:
            db.session.rollback()
            return False

    @staticmethod
    def update_status(status_id: int, new_status: str, user_email: str) -> bool:
        try:
            status = Status.query.get(status_id)
            if status:
                status.status = new_status
                status.updated_at = db.func.now()
                StatusRepository.update(status)
                EmailNotificationService.send_notification(user_email, "Status Update", f"Your request status has been updated to: {new_status}")
                return True
            return False
        except Exception as e:
            db.session.rollback()
            return False


# File 4: Update Status Controller to Include Email in status/controllers/status_controller.py