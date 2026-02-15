# Epic Title: In-app Notifications

from backend.repositories.notifications.in_app_notification_repository import InAppNotificationRepository
from backend.models.notifications.in_app_notification_model import InAppNotification

class InAppNotificationService:
    @staticmethod
    def create_notification(user_id: int, message: str) -> None:
        notification = InAppNotification(user_id=user_id, message=message)
        InAppNotificationRepository.save(notification)

    @staticmethod
    def mark_notification_as_seen(notification_id: int) -> None:
        InAppNotificationRepository.mark_as_seen(notification_id)

    @staticmethod
    def get_unseen_notifications(user_id: int) -> list[InAppNotification]:
        return InAppNotificationRepository.find_unseen_by_user_id(user_id)


# File 4: In-App Notification Controller in `controllers/notifications/in_app_notification_controller.py`