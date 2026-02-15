# Epic Title: Create Secure User Sessions

from flask import Blueprint, request, jsonify, session
from flask_login import login_user, current_user, logout_user
from backend.services.authentication.mfa_service import MFAService
from backend.repositories.authentication.user_repository import UserRepository
from backend.models.authentication.user_model import User

authentication_controller = Blueprint('authentication_controller', __name__)

@authentication_controller.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    user = UserRepository.find_by_username(username)
    if user and user.check_password(password):
        session['pre_mfa_user_id'] = user.id
        session.permanent = True
        return jsonify({'message': 'Password correct, enter MFA token'}), 200

    return jsonify({'message': 'Invalid username or password'}), 401

@authentication_controller.route('/mfa', methods=['POST'])
def mfa():
    data = request.get_json()
    otp = data.get('mfa_token')

    user_id = session.get('pre_mfa_user_id')
    if not user_id:
        return jsonify({'message': 'MFA session invalid'}), 401

    user = User.query.get(user_id)
    if not user:
        return jsonify({'message': 'User not found'}), 404

    if MFAService.verify_otp(user.mfa_secret, otp):
        login_user(user)
        session['last_activity'] = int(datetime.utcnow().timestamp())
        return jsonify({'message': 'Login successful'}), 200

    return jsonify({'message': 'Invalid MFA token'}), 401

@authentication_controller.route('/logout', methods=['POST'])
def logout():
    logout_user()
    session.clear()
    return jsonify({'message': 'Logged out successfully'}), 200


# File 3: Update app.py to Apply Session Middleware