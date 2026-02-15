# Epic Title: Real-time Status Updates and Notifications

from backend.models.notifications.in_app_notification_model import InAppNotification
from backend.app import db

class InAppNotificationRepository:
    @staticmethod
    def save(notification: InAppNotification) -> None:
        db.session.add(notification)
        db.session.commit()

    @staticmethod
    def get_by_user_id(user_id: int) -> list[InAppNotification]:
        return InAppNotification.query.filter_by(user_id=user_id, seen=0).all()

    @staticmethod
    def mark_as_seen(notification_id: int) -> None:
        notification = InAppNotification.query.get(notification_id)
        if notification:
            notification.seen = 1
            db.session.commit()

# File 3: Notification Service in services/notifications/in_app_notification_service.py