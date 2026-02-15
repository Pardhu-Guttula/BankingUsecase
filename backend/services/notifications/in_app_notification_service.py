# Epic Title: Real-time Status Updates and Notifications

from backend.models.notifications.in_app_notification_model import InAppNotification
from backend.repositories.notifications.in_app_notification_repository import InAppNotificationRepository

class InAppNotificationService:
    @staticmethod
    def create_notification(user_id: int, message: str) -> InAppNotification:
        notification = InAppNotification(user_id=user_id, message=message)
        InAppNotificationRepository.save(notification)
        return notification

    @staticmethod
    def get_user_notifications(user_id: int) -> list[InAppNotification]:
        return InAppNotificationRepository.get_by_user_id(user_id)

    @staticmethod
    def mark_notification_as_seen(notification_id: int) -> None:
        InAppNotificationRepository.mark_as_seen(notification_id)

# File 4: Update Request Status Service to Create In-App Notifications in services/status/request_status_service.py (Modified)