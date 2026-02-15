# Epic Title: User Authentication and Security

from flask import Blueprint, request, jsonify, session
from flask_login import login_required, logout_user, login_user
from backend.services.authentication.authentication_service import AuthenticationService
from datetime import datetime

authentication_controller = Blueprint('authentication_controller', __name__)

@authentication_controller.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    user = AuthenticationService.authenticate(username, password)
    if user:
        if user.mfa_enabled:
            return jsonify({'message': 'MFA required', 'mfa_enabled': True}), 200
        else:
            login_user(user)
            session['last_activity'] = datetime.utcnow()
            return jsonify({'message': 'Login successful', 'mfa_enabled': False}), 200

    return jsonify({'message': 'Invalid credentials'}), 401

@authentication_controller.route('/login/mfa', methods=['POST'])
def login_mfa():
    data = request.get_json()
    token = data.get('token')
    user_id = session.get('pre_mfa_user_id')

    if not user_id:
        return jsonify({'message': 'Session expired, please login again'}), 401

    if AuthenticationService.login_user_with_mfa(user_id, token):
        session['last_activity'] = datetime.utcnow()
        return jsonify({'message': 'Login successful'}), 200

    return jsonify({'message': 'Invalid MFA token'}), 401

@authentication_controller.route('/logout', methods=['POST'])
@login_required
def logout():
    logout_user()
    return jsonify({'message': 'Logout successful'}), 200

# File 5: Register Middlewares and Authentication Controller Blueprint in app.py (Already Exists, Modified)