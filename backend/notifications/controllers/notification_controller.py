# Epic Title: Email Notifications

from flask import Blueprint, request, jsonify
from notifications.services.email_service import EmailService

notification_controller = Blueprint('notification_controller', __name__)

email_service = EmailService(
    smtp_server='smtp.example.com', 
    smtp_port=587, 
    username='your_email@example.com', 
    password='your_password'
)

@notification_controller.route('/notify', methods=['POST'])
def notify():
    data = request.json
    user_id = data.get('user_id')
    message = data.get('message')
    email = data.get('email')  # Email address is provided in the request

    if not user_id or not message or not email:
        return jsonify({"error": "user_id, message, and email are required"}), 400

    # Send real-time notification
    redis_client.publish('updates', json.dumps({'user_id': user_id, 'message': message}))

    # Send email notification
    email_subject = "Update on Your Request"
    email_body = f"Hello,\n\nThere has been an update on your request:\n\n{message}\n\nBest regards,\nYour Portal Team"
    email_service.send_email(email, email_subject, email_body)
    
    return jsonify({"message": "Notification sent"}), 200


# File 3: requirements.txt Update