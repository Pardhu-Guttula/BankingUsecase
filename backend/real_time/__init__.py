# Epic Title: Real-time Status Updates

import redis
import json
from flask_socketio import SocketIO
from threading import Thread

socketio = SocketIO()
redis_client = redis.StrictRedis(host='localhost', port=6379, db=0, decode_responses=True)

def notify_user(user_id, message):
    socketio.emit(f'user_{user_id}', message)

def listen_for_updates():
    pubsub = redis_client.pubsub()
    pubsub.subscribe('updates')
    for message in pubsub.listen():
        if message['type'] == 'message':
            data = json.loads(message['data'])
            notify_user(data['user_id'], data['message'])

def start_listener():
    thread = Thread(target=listen_for_updates)
    thread.daemon = True
    thread.start()


# File 2: Real-time Update Endpoint in real_time/controllers/notification_controller.py