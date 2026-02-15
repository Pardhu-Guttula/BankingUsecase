# Epic Title: Core Banking System Integration

from flask import request, jsonify
from functools import wraps
import jwt
from datetime import datetime, timedelta

SECRET_KEY = 'yoursecretkey'  # Should be stored securely, e.g., in environment variables

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None
        if 'x-access-tokens' in request.headers:
            token = request.headers['x-access-tokens']
        if not token:
            return jsonify({'message': 'Token is missing!'}), 401
        try:
            data = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
            current_user = data['user_id']
        except Exception as e:
            return jsonify({'message': str(e)}), 401
        
        return f(current_user, *args, **kwargs)
    
    return decorated

def generate_token(user_id):
    token = jwt.encode({
        'user_id': user_id,
        'exp': datetime.utcnow() + timedelta(minutes=60)
    }, SECRET_KEY, algorithm="HS256")
    return token


# File 2: Core Banking API Controller in integration/controllers/core_banking_api_controller.py