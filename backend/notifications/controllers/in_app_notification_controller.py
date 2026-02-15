# Epic Title: Real-time Status Updates and Notifications

from flask import Blueprint, jsonify
from flask_login import login_required, current_user
from backend.services.notifications.in_app_notification_service import InAppNotificationService

in_app_notification_controller = Blueprint('in_app_notification_controller', __name__)

@in_app_notification_controller.route('/notifications', methods=['GET'])
@login_required
def get_user_notifications():
    notifications = InAppNotificationService.get_user_notifications(current_user.id)
    return jsonify([{
        'message': notification.message,
        'created_at': notification.created_at
    } for notification in notifications])


# File 6: Update Main App to Register In-App Notification Controller Blueprint in app.py (Already Exists, Modified)