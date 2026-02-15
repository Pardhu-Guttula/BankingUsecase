# Epic Title: Real-time Status Updates and Notifications

from flask import Blueprint, jsonify, request
from flask_login import login_required, current_user
from backend.services.notifications.in_app_notification_service import InAppNotificationService

in_app_notification_controller = Blueprint('in_app_notification_controller', __name__)

@in_app_notification_controller.route('/notifications', methods=['GET'])
@login_required
def get_notifications():
    user_id = current_user.id
    notifications = InAppNotificationService.get_notifications(user_id)
    notifications_list = [{
        'id': notification.id,
        'request_id': notification.request_id,
        'message': notification.message,
        'created_at': notification.created_at
    } for notification in notifications]
    return jsonify(notifications_list)

# File 3: Notification Model in models/notifications/notification_model.py (Already Exists, Modified)