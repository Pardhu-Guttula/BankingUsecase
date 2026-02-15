# Epic Title: Real-time Status Updates and Notifications

from backend.models.notifications.notification_model import Notification
from backend.repositories.notifications.notification_repository import NotificationRepository

class InAppNotificationService:
    @staticmethod
    def create_notification(user_id: int, request_id: int, message: str) -> Notification:
        notification = Notification(user_id=user_id, request_id=request_id, message=message)
        NotificationRepository.save(notification)
        return notification

    @staticmethod
    def get_notifications(user_id: int) -> list[Notification]:
        return NotificationRepository.get_notifications_by_user_id(user_id)

# File 2: In-App Notification Controller in notifications/controllers/in_app_notification_controller.py