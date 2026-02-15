# Epic Title: In-app Notifications

from flask import Blueprint, request, jsonify
from flask_login import login_required, current_user
from backend.services.notifications.in_app_notification_service import InAppNotificationService

in_app_notification_controller = Blueprint('in_app_notification_controller', __name__)

@in_app_notification_controller.route('/notifications/in-app', methods=['POST'])
@login_required
def create_in_app_notification():
    data = request.get_json()
    user_id = data.get('user_id')
    message = data.get('message')

    if not user_id or not message:
        return jsonify({'message': 'User ID and message are required'}), 400

    InAppNotificationService.create_notification(user_id, message)
    return jsonify({'message': 'In-app notification created successfully'}), 201

@in_app_notification_controller.route('/notifications/in-app/<int:user_id>', methods=['GET'])
@login_required
def get_in_app_notifications(user_id: int):
    notifications = InAppNotificationService.get_unseen_notifications(user_id)
    return jsonify({'notifications': [notification.serialize() for notification in notifications]}), 200

@in_app_notification_controller.route('/notifications/in-app/mark-seen/<int:notification_id>', methods=['PUT'])
@login_required
def mark_notification_as_seen(notification_id: int):
    InAppNotificationService.mark_notification_as_seen(notification_id)
    return jsonify({'message': 'In-app notification marked as seen'}), 200


# File 5: Schema for In-App Notifications Table in `database/create_in_app_notifications_table.sql`