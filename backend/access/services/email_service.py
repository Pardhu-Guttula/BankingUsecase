import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import logging
import requests  # New import to fetch user's email

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

    def fetch_user_email(self, user_id: int) -> str:
        # Simulating an API call to fetch the user's email
        try:
            response = requests.get(f"https://example.com/api/users/{user_id}")
            response.raise_for_status()
            user_data = response.json()
            return user_data.get("email")
        except Exception as e:
            logger.error(f"Failed to fetch user email for user_id {user_id}: {e}")
            return ""

    def send_status_update_email(self, user_id: int, request_id: int, status: str):
        to_email = self.fetch_user_email(user_id)
        if to_email:
            subject = f"Status Update for Request {request_id}"
            body = f"Dear User,\n\nThe status of your request #{request_id} has been updated to '{status}'.\n\nThank you."
            self.send_email(to_email, subject, body)
        else:
            logger.error(f"Could not send status update email. No email found for user_id {user_id}.")