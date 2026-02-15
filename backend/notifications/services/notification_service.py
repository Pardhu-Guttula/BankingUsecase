# Epic Title: Real-time Status Updates and Notifications

from backend.models.notifications.notification_model import Notification
from backend.notifications.repositories.notification_repository import NotificationRepository
from backend.app import db

class NotificationService:
    @staticmethod
    def create_notification(user_id: int, message: str) -> bool:
        try:
            notification = Notification(user_id=user_id, message=message)
            NotificationRepository.save(notification)
            return True
        except Exception as e:
            db.session.rollback()
            return False

    @staticmethod
    def mark_notification_as_read(notification_id: int) -> bool:
        try:
            NotificationRepository.mark_as_read(notification_id)
            return True
        except Exception as e:
            db.session.rollback()
            return False

    @staticmethod
    def get_unread_notifications(user_id: int) -> list[Notification]:
        return NotificationRepository.get_unread_notifications(user_id)


# File 4: Notification Controller to Expose Notification Endpoints in notifications/controllers/notification_controller.py