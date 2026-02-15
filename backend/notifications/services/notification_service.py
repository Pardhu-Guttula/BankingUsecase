# Epic Title: In-app Notifications

import redis
import json

class NotificationService:
    def __init__(self, redis_host: str = 'localhost', redis_port: int = 6379):
        self.redis_client = redis.StrictRedis(host=redis_host, port=redis_port, db=0, decode_responses=True)

    def send_notification(self, user_id: int, message: str):
        notification_data = {
            'user_id': user_id,
            'message': message
        }
        self.redis_client.publish('in_app_notifications', json.dumps(notification_data))


# File 2: In-app Notification Endpoint in notifications/controllers/notification_controller.py