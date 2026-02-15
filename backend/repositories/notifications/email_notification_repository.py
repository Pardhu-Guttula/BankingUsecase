# Epic Title: Real-time Status Updates and Notifications

from backend.models.notifications.email_notification_model import EmailNotification
from backend.app import db

class EmailNotificationRepository:
    @staticmethod
    def save(email_notification: EmailNotification) -> None:
        db.session.add(email_notification)
        db.session.commit()

    @staticmethod
    def mark_as_sent(email_notification: EmailNotification) -> None:
        email_notification.sent = True
        db.session.commit()


# File 4: Email Notification Service Layer in services/notifications/email_notification_service.py