# Epic Title: Real-time Status Updates and Notifications

from dashboard.repositories.notification_repository import NotificationRepository
from dashboard.models.notification_model import Notification

class NotificationService:
    @staticmethod
    def create_notification(user_id: int, message: str) -> Notification:
        notification = Notification(user_id=user_id, message=message)
        NotificationRepository.save(notification)
        return notification

    @staticmethod
    def get_user_notifications(user_id: int) -> list:
        notifications = NotificationRepository.get_notifications_by_user_id(user_id)
        return [{
            "id": notification.id,
            "message": notification.message,
            "is_read": notification.is_read,
            "created_at": notification.created_at
        } for notification in notifications]

    @staticmethod
    def mark_notification_as_read(notification_id: int) -> None:
        NotificationRepository.mark_as_read(notification_id)


# File 4: Notification Controller for Handling Requests in dashboard/controllers/notification_controller.py