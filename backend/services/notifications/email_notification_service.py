# Epic Title: Email Notifications

from backend.repositories.notifications.email_notification_repository import EmailNotificationRepository
from backend.models.notifications.email_notification_model import EmailNotification
from flask_mail import Message
from backend.app import mail

class EmailNotificationService:
    @staticmethod
    def send_email_notification(user_id: int, email: str, subject: str, body: str) -> None:
        notification = EmailNotification(user_id=user_id, subject=subject, body=body)
        EmailNotificationRepository.save(notification)

        msg = Message(
            subject=subject,
            recipients=[email],
            body=body,
            sender='no-reply@yourdomain.com'
        )
        mail.send(msg)


# File 4: Email Notification Controller in controllers/notifications/email_notification_controller.py