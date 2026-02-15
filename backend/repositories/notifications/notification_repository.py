# Epic Title: Real-time Status Updates and Notifications

from backend.models.notifications.notification_model import Notification
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
    def delete(notification: Notification) -> None:
        db.session.delete(notification)
        db.session.commit()

# File 3: Notification Service to Handle Business Logic in services/notifications/notification_service.py