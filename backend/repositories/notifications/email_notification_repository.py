# Epic Title: Real-time Status Updates and Notifications

from backend.models.notifications.email_notification_model import EmailNotification
from backend.app import db


class EmailNotificationRepository:
    @staticmethod
    def save(email_notification: EmailNotification) -> None:
        db.session.add(email_notification)
        db.session.commit()

    @staticmethod
    def get_notifications_by_user(user_id: int) -> list[EmailNotification]:
        return EmailNotification.query.filter_by(user_id=user_id).all()


# File 3: Notification Service to Handle Email Logic in services/notifications/email_notification_service.py