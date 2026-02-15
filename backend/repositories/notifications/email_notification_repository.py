# Epic Title: Email Notifications

from backend.models.notifications.email_notification_model import EmailNotification
from backend.app import db

class EmailNotificationRepository:
    @staticmethod
    def save(notification: EmailNotification) -> None:
        db.session.add(notification)
        db.session.commit()

    @staticmethod
    def find_by_user_id(user_id: int) -> list[EmailNotification]:
        return EmailNotification.query.filter_by(user_id=user_id).all()


# File 3: Email Notification Service in `services/notifications/email_notification_service.py`