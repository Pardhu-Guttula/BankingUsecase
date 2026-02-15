# Epic Title: User Authentication and Security

from flask import Blueprint, request, jsonify, session
from flask_login import login_user, current_user
from backend.services.authentication.authentication_service import AuthenticationService

authentication_controller = Blueprint('authentication_controller', __name__)

@authentication_controller.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    user = AuthenticationService.validate_user_credentials(data['username'], data['password'])
    if not user:
        return jsonify({"error": "Invalid username or password"}), 401

    if user.is_2fa_enabled:
        session['user_id'] = user.id
        session['2fa_required'] = True
        return jsonify({"message": "2FA required"}), 200
    else:
        login_user(user)
        return jsonify({"message": "Logged in successfully"}), 200

@authentication_controller.route('/verify-2fa', methods=['POST'])
def verify_2fa():
    if not session.get('2fa_required'):
        return jsonify({"error": "2FA not required"}), 400

    user = User.query.get(session['user_id'])
    token = request.get_json().get('token')
    if AuthenticationService.validate_mfa_token(user, token):
        login_user(user)
        session.pop('2fa_required', None)
        return jsonify({"message": "Logged in successfully"}), 200
    return jsonify({"error": "Invalid 2FA token"}), 401


# File 5: Middleware for 2FA Session Management in middleware/session_middleware.py