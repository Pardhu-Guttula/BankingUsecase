# Epic Title: Real-time Status Updates and Notifications

from flask import Blueprint, jsonify, request
from flask_login import login_required, current_user
from dashboard.services.notification_service import NotificationService

notification_controller = Blueprint('notification_controller', __name__)

@notification_controller.route('/notifications', methods=['GET'])
@login_required
def get_notifications():
    notifications = NotificationService.get_user_notifications(current_user.id)
    return jsonify(notifications), 200

@notification_controller.route('/notifications/<int:notification_id>/read', methods=['POST'])
@login_required
def mark_as_read(notification_id: int):
    NotificationService.mark_notification_as_read(notification_id)
    return jsonify({"message": "Notification marked as read"}), 200


# File 5: App Update to Register Notification Controller in app.py