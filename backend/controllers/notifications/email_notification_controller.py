# Epic Title: Email Notifications

from flask import Blueprint, request, jsonify
from flask_login import login_required, current_user
from backend.services.notifications.email_notification_service import EmailNotificationService

email_notification_controller = Blueprint('email_notification_controller', __name__)

@email_notification_controller.route('/notifications/email', methods=['POST'])
@login_required
def send_email_notification():
    data = request.get_json()
    user_id = data.get('user_id')
    email = data.get('email')
    subject = data.get('subject')
    body = data.get('body')

    if not user_id or not email or not subject or not body:
        return jsonify({'message': 'User ID, email, subject, and body are required'}), 400

    EmailNotificationService.send_email_notification(user_id, email, subject, body)
    return jsonify({'message': 'Email notification sent successfully'}), 201

@email_notification_controller.route('/notifications/email/<int:user_id>', methods=['GET'])
@login_required
def get_email_notifications(user_id: int):
    notifications = EmailNotificationRepository.find_by_user_id(user_id)
    return jsonify({'notifications': [notification.serialize() for notification in notifications]}), 200


# File 5: Schema for Email Notifications Table in `database/create_email_notifications_table.sql`