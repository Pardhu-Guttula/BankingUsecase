# Epic Title: Real-time Status Updates and Notifications

from dashboard.models.notification_model import Notification
from backend.app import db

class NotificationRepository:
    @staticmethod
    def save(notification: Notification) -> None:
        db.session.add(notification)
        db.session.commit()

    @staticmethod
    def get_notifications_by_user_id(user_id: int) -> list[Notification]:
        return Notification.query.filter_by(user_id=user_id).order_by(Notification.created_at.desc()).all()

    @staticmethod
    def mark_as_read(notification_id: int) -> None:
        notification = Notification.query.get(notification_id)
        if notification:
            notification.is_read = True
            db.session.commit()


# File 3: Notification Service for Business Logic in dashboard/services/notification_service.py