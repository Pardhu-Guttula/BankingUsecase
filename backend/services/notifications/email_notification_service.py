# Epic Title: Real-time Status Updates and Notifications

from flask_mail import Message
from flask import current_app
from backend.models.notifications.email_notification_model import EmailNotification
from backend.repositories.notifications.email_notification_repository import EmailNotificationRepository
from backend.app import mail

class EmailNotificationService:
    @staticmethod
    def send_email(user_id: int, email: str, subject: str, content: str) -> None:
        msg = Message(subject, recipients=[email], body=content, sender=current_app.config['MAIL_USERNAME'])
        mail.send(msg)
        email_notification = EmailNotification(user_id=user_id, subject=subject, content=content)
        EmailNotificationRepository.save(email_notification)

    @staticmethod
    def get_user_notifications(user_id: int) -> list[EmailNotification]:
        return EmailNotificationRepository.get_notifications_by_user(user_id)


# File 4: Update Request Status Service to Trigger Email Notifications in services/status/request_status_service.py (Already Exists, Modified)