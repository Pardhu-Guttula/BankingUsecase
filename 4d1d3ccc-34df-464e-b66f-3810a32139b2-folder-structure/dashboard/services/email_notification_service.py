# Epic Title: Real-time Status Updates and Notifications

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

class EmailNotificationService:
    @staticmethod
    def send_email(to: str, subject: str, body: str) -> None:
        from_email = "your-email@example.com"
        from_password = "your-email-password"

        msg = MIMEMultipart()
        msg['From'] = from_email
        msg['To'] = to
        msg['Subject'] = subject

        msg.attach(MIMEText(body, 'plain'))

        try:
            server = smtplib.SMTP('smtp.example.com', 587)
            server.starttls()
            server.login(from_email, from_password)
            server.sendmail(from_email, to, msg.as_string())
            server.quit()
        except Exception as e:
            print(f"Failed to send email: {e}")

# File 2: Modified Status Update Service to Include Email Notifications in dashboard/services/status_update_service.py