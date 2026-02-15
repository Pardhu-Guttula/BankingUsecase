# Epic Title: Real-time Status Updates

from flask import Blueprint, request, jsonify
from .. import redis_client

notification_controller = Blueprint('notification_controller', __name__)

@notification_controller.route('/notify', methods=['POST'])
def notify():
    data = request.json
    user_id = data.get('user_id')
    message = data.get('message')
    
    if not user_id or not message:
        return jsonify({"error": "user_id and message are required"}), 400
    
    redis_client.publish('updates', json.dumps({'user_id': user_id, 'message': message}))
    
    return jsonify({"message": "Notification sent"}), 200


# File 3: SocketIO Client Script in static/js/socket.js