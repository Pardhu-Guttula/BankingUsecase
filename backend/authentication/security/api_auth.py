# Epic Title: Core Banking System Integration

from functools import wraps
from flask import request, jsonify
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer, BadSignature, SignatureExpired
from backend.app import app

def generate_token(user_id: int) -> str:
    s = Serializer(app.config['SECRET_KEY'], expires_in=3600)
    return s.dumps({'user_id': user_id}).decode('utf-8')

def verify_token(token: str) -> int | None:
    s = Serializer(app.config['SECRET_KEY'])
    try:
        data = s.loads(token)
    except (SignatureExpired, BadSignature):
        return None
    return data['user_id']

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.headers.get('Authorization')
        if not token:
            return jsonify({'message': 'Token is missing!'}), 401
        user_id = verify_token(token)
        if user_id is None:
            return jsonify({'message': 'Token is invalid!'}), 401
        return f(user_id, *args, **kwargs)
    return decorated

# File 2: Core Banking API Route in routes/core_banking_api_route.py