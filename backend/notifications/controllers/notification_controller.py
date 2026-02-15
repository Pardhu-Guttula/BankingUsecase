# Epic Title: Real-time Status Updates and Notifications

from flask import Blueprint, jsonify
from flask_login import login_required, current_user
from backend.notifications.services.notification_service import NotificationService

notification_controller = Blueprint('notification_controller', __name__)

@notification_controller.route('/notifications/unread', methods=['GET'])
@login_required
def get_unread_notifications():
    notifications = NotificationService.get_unread_notifications(current_user.id)
    return jsonify([{"id": n.id, "message": n.message, "created_at": n.created_at.strftime("%Y-%m-%d %H:%M:%S")} for n in notifications])

@notification_controller.route('/notifications/read/<int:notification_id>', methods=['PUT'])
@login_required
def mark_notification_as_read(notification_id):
    if NotificationService.mark_notification_as_read(notification_id):
        return jsonify({"message": "Notification marked as read."}), 200
    return jsonify({"message": "Failed to mark notification as read."}), 500


# File 5: Update Status Service to Trigger In-App Notifications in status/services/status_service.py