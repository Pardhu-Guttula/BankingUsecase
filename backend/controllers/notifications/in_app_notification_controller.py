# Epic Title: Real-time Status Updates and Notifications

from flask import Blueprint, jsonify
from flask_login import login_required, current_user
from backend.services.notifications.in_app_notification_service import InAppNotificationService

in_app_notification_controller = Blueprint('in_app_notification_controller', __name__)

@in_app_notification_controller.route('/notifications', methods=['GET'])
@login_required
def get_notifications():
    notifications = InAppNotificationService.get_user_notifications(current_user.id)
    notifications_list = [{
        'id': n.id,
        'user_id': n.user_id,
        'message': n.message,
        'timestamp': n.timestamp,
        'seen': n.seen
    } for n in notifications]
    return jsonify(notifications_list)

@in_app_notification_controller.route('/notifications/<int:notification_id>/seen', methods=['PUT'])
@login_required
def mark_notification_as_seen(notification_id: int):
    InAppNotificationService.mark_notification_as_seen(notification_id)
    return jsonify({'message': 'Notification marked as seen'})

# File 6: Register Notification Controller Blueprint in app.py (Already Exists, Modified)