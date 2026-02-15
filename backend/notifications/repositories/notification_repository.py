# Epic Title: Real-time Status Updates and Notifications

from backend.models.notifications.notification_model import Notification
from backend.app import db

class NotificationRepository:
    @staticmethod
    def save(notification: Notification) -> None:
        db.session.add(notification)
        db.session.commit()

    @staticmethod
    def mark_as_read(notification_id: int) -> None:
        notification = Notification.query.get(notification_id)
        if notification:
            notification.is_read = True
            db.session.commit()

    @staticmethod
    def get_unread_notifications(user_id: int) -> list[Notification]:
        return Notification.query.filter_by(user_id=user_id, is_read=False).all()


# File 3: Notification Service to Handle Business Logic in notifications/services/notification_service.py