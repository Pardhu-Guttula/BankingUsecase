# Epic Title: Real-time Status Updates and Notifications

from backend.repositories.notifications.email_notification_repository import EmailNotificationRepository
from backend.models.notifications.email_notification_model import EmailNotification
from flask_mail import Message
from backend.app import mail

class EmailNotificationService:
    @staticmethod
    def create_notification(request_id: int, user_id: int, email: str, subject: str, content: str) -> EmailNotification:
        email_notification = EmailNotification(request_id=request_id, user_id=user_id, email=email, subject=subject, content=content)
        EmailNotificationRepository.save(email_notification)
        return email_notification

    @staticmethod
    def send_email(email_notification: EmailNotification) -> None:
        msg = Message(email_notification.subject, sender='no-reply@example.com', recipients=[email_notification.email])
        msg.body = email_notification.content
        mail.send(msg)
        EmailNotificationRepository.mark_as_sent(email_notification)


# File 5: Integrate Email Notifications with Request Status Service in services/status/request_status_service.py (Update)