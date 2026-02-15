# Epic Title: Real-time Status Updates and Notifications

from backend.models.notifications.status_update_model import StatusUpdate
from backend.repositories.notifications.status_update_repository import StatusUpdateRepository

class InAppNotificationService:
    @staticmethod
    def mark_as_read(update_id: int) -> None:
        update = StatusUpdateRepository.find_by_id(update_id)
        if update:
            update.is_read = True
            StatusUpdateRepository.save(update)

    @staticmethod
    def get_unread_notifications(user_id: int) -> list[StatusUpdate]:
        return StatusUpdateRepository.find_unread_by_user_id(user_id)


# File 3: Update `StatusUpdateService` to Use In-App Notifications in services/notifications/status_update_service.py