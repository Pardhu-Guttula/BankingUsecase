# Epic Title: Real-time Status Updates and Notifications

from flask import current_app
from flask_mail import Message, Mail

mail = Mail()

class EmailNotificationService:
    @staticmethod
    def send_notification(email: str, subject: str, body: str) -> bool:
        try:
            msg = Message(subject, sender=current_app.config['MAIL_USERNAME'], recipients=[email])
            msg.body = body
            mail.send(msg)
            return True
        except Exception as e:
            current_app.logger.error(f"Failed to send email: {e}")
            return False


# File 2: Email Notification Configuration and Initialization in app.py