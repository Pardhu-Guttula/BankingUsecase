# Epic Title: Real-time Status Updates and Notifications

from backend.models.notifications.in_app_notification_model import InAppNotification
from backend.app import db

class InAppNotificationRepository:
    @staticmethod
    def save(in_app_notification: InAppNotification) -> None:
        db.session.add(in_app_notification)
        db.session.commit()

    @staticmethod
    def mark_as_read(in_app_notification: InAppNotification) -> None:
        in_app_notification.is_read = True
        db.session.commit()


# File 4: In-App Notification Service Layer in services/notifications/in_app_notification_service.py