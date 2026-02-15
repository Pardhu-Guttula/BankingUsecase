# Epic Title: Real-time Status Updates and Notifications

from dashboard.repositories.status_update_repository import StatusUpdateRepository
from dashboard.models.status_update_model import StatusUpdate
from dashboard.services.email_notification_service import EmailNotificationService

class StatusUpdateService:
    @staticmethod
    def create_status_update(request_id: int, status: str, user_email: str) -> StatusUpdate:
        status_update = StatusUpdate(request_id, status)
        StatusUpdateRepository.save(status_update)

        # Send email notification
        EmailNotificationService.send_email(
            to=user_email,
            subject="Status Update Notification",
            body=f"Your request (ID: {request_id}) status has been updated to '{status}'."
        )
        return status_update

    @staticmethod
    def get_request_status_updates(request_id: int) -> list:
        updates = StatusUpdateRepository.get_updates_by_request_id(request_id)
        return [{
            "id": update.id,
            "status": update.status,
            "updated_at": update.updated_at
        } for update in updates]


# File 3: App Update to Register Updated Status Update Service in app.py