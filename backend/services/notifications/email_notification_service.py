# Epic Title: Real-time Status Updates and Notifications

import smtplib
from email.mime.text import MIMEText
from backend.models.notifications.status_update_model import StatusUpdate

class EmailNotificationService:
    @staticmethod
    def send_email_notification(to_email: str, subject: str, message: str) -> None:
        msg = MIMEText(message)
        msg["Subject"] = subject
        msg["From"] = "no-reply@myportal.com"
        msg["To"] = to_email

        with smtplib.SMTP("smtp.example.com", 587) as server:
            server.starttls()
            server.login("your-email@example.com", "your-email-password")
            server.send_message(msg)

    @staticmethod
    def send_status_update_email(user_email: str, status_update: StatusUpdate) -> None:
        subject = f"Update on your request #{status_update.request_id}"
        message = f"Dear user,\n\nThere is an update on your request:\n\n{status_update.update_message}\n\nStatus: {status_update.status}\n\nBest Regards,\nMyPortal Team"
        EmailNotificationService.send_email_notification(user_email, subject, message)


# File 3: Update `StatusUpdateService` to Use Email Notification Service in services/notifications/status_update_service.py