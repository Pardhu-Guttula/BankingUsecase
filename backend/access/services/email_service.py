# Epic Title: Real-time Status Updates and Notifications

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import logging

logger = logging.getLogger(__name__)

class EmailService:
    def __init__(self, smtp_server: str, smtp_port: int, username: str, password: str):
        self.smtp_server = smtp_server
        self.smtp_port = smtp_port
        self.username = username
        self.password = password

    def send_email(self, to_email: str, subject: str, body: str):
        try:
            msg = MIMEMultipart()
            msg['From'] = self.username
            msg['To'] = to_email
            msg['Subject'] = subject

            msg.attach(MIMEText(body, 'plain'))
            server = smtplib.SMTP(self.smtp_server, self.smtp_port)
            server.starttls()
            server.login(self.username, self.password)
            text = msg.as_string()
            server.sendmail(self.username, to_email, text)
            server.quit()
            
            logger.info(f"Email sent to {to_email} with subject '{subject}'")
        except Exception as e:
            logger.error(f"Failed to send email: {e}")

    def send_status_update_email(self, user_id: int, request_id: int, status: str):
        # Fetch user's email based on user_id (dummy email for this example)
        to_email = "user@example.com"
        subject = f"Status Update for Request {request_id}"
        body = f"Dear User,\n\nThe status of your request #{request_id} has been updated to '{status}'.\n\nThank you."
        self.send_email(to_email, subject, body)