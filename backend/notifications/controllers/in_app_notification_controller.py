# Epic Title: Real-time Status Updates and Notifications

from flask import Blueprint, jsonify
from flask_login import login_required, current_user
from backend.models.notifications.in_app_notification_model import InAppNotification

in_app_notification_controller = Blueprint('in_app_notification_controller', __name__)

@in_app_notification_controller.route('/notifications', methods=['GET'])
@login_required
def get_notifications():
    notifications = InAppNotification.query.filter_by(user_id=current_user.id, is_read=False).all()
    notifications_data = [{
        "id": n.id,
        "request_id": n.request_id,
        "message": n.message,
        "timestamp": n.timestamp
    } for n in notifications]
    return jsonify(notifications_data), 200

@in_app_notification_controller.route('/notifications/<int:notification_id>/read', methods=['POST'])
@login_required
def mark_notification_as_read(notification_id):
    InAppNotificationService.mark_notification_as_read(notification_id)
    return jsonify({"message": "Notification marked as read"}), 200


# File 7: Update Main App to Register In-App Notification Controller in app.py