# Epic Title: Real-time Status Updates and Notifications

from backend.models.notifications.notification_model import Notification
from backend.repositories.notifications.notification_repository import NotificationRepository
from flask_mail import Message
from backend.app import mail

class NotificationService:
    @staticmethod
    def send_notification(user_id: int, request_id: int, message: str) -> Notification:
        notification = Notification(user_id=user_id, request_id=request_id, message=message)
        NotificationRepository.save(notification)
        return notification

    @staticmethod
    def get_notifications(user_id: int) -> list[Notification]:
        return NotificationRepository.get_notifications_by_user_id(user_id)

    @staticmethod
    def send_email_notification(to_email: str, subject: str, body: str) -> None:
        msg = Message(subject, recipients=[to_email], body=body)
        mail.send(msg)

# File 4: Status Service Update to Send Email Notification in services/status/status_service.py (Already Exists, Modified)