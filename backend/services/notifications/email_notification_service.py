# Epic Title: Real-time Status Updates and Notifications

from flask_mail import Message
from backend.app import mail
from typing import List

class EmailNotificationService:
    @staticmethod
    def send_email(subject: str, recipients: List[str], body: str) -> None:
        msg = Message(subject, recipients=recipients, body=body)
        mail.send(msg)

# File 2: Update Request Status Service to Send Email Notifications in services/status/request_status_service.py (Modified)