# Epic Title: Real-time Status Updates and Notifications

from backend.models.notifications.in_app_notification_model import InAppNotification
from backend.app import db


class InAppNotificationRepository:
    @staticmethod
    def save(in_app_notification: InAppNotification) -> None:
        db.session.add(in_app_notification)
        db.session.commit()

    @staticmethod
    def get_notifications_by_user(user_id: int) -> list[InAppNotification]:
        return InAppNotification.query.filter_by(user_id=user_id).all()


# File 3: In-App Notification Service to Handle Notification Logic in services/notifications/in_app_notification_service.py