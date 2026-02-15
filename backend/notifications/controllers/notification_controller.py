# Epic Title: In-app Notifications

from flask import Blueprint, request, jsonify
from notifications.services.notification_service import NotificationService

notification_controller = Blueprint('notification_controller', __name__)
notification_service = NotificationService()

@notification_controller.route('/notify', methods=['POST'])
def notify():
    data = request.json
    user_id = data.get('user_id')
    message = data.get('message')
    
    if not user_id or not message:
        return jsonify({"error": "user_id and message are required"}), 400

    # Send in-app notification
    notification_service.send_notification(user_id, message)
    
    return jsonify({"message": "Notification sent"}), 200


# File 3: HTML for In-app Notifications in templates/notification.html