# Epic Title: Core Banking System Integration

from flask import request, jsonify
from jwt import decode, exceptions
from functools import wraps

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None
        if 'x-access-token' in request.headers:
            token = request.headers['x-access-token']
        
        if not token:
            return jsonify({"message": "Token is missing!"}), 401

        try:
            data = decode(token, current_app.config['JWT_SECRET_KEY'], algorithms=["HS256"])
            current_user = data['user_id']
        except exceptions.ExpiredSignatureError:
            return jsonify({"message": "Token expired!"}), 401
        except exceptions.InvalidTokenError:
            return jsonify({"message": "Invalid token!"}), 401

        return f(current_user, *args, **kwargs)

    return decorated