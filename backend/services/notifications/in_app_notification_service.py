# Epic Title: Real-time Status Updates and Notifications

from backend.models.notifications.in_app_notification_model import InAppNotification
from backend.repositories.notifications.in_app_notification_repository import InAppNotificationRepository


class InAppNotificationService:
    @staticmethod
    def create_notification(user_id: int, message: str) -> None:
        notification = InAppNotification(user_id=user_id, message=message)
        InAppNotificationRepository.save(notification)

    @staticmethod
    def get_user_notifications(user_id: int) -> list[InAppNotification]:
        return InAppNotificationRepository.get_notifications_by_user(user_id)


# File 4: Update Request Status Service to Trigger In-App Notifications in services/status/request_status_service.py (Already Exists, Modified)