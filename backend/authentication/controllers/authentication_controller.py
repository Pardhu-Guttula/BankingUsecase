# Epic Title: User Authentication and Security

from flask import Blueprint, request, jsonify, session
from flask_login import login_user, current_user
from backend.authentication.services.authentication_service import AuthenticationService
from backend.authentication.repositories.user_repository import UserRepository
from backend.models.authentication.user_model import User

authentication_controller = Blueprint('authentication_controller', __name__)

@authentication_controller.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    if not username or not password:
        return jsonify({"message": "Username and password are required"}), 400

    if AuthenticationService.authenticate(username, password):
        user = UserRepository.get_user_by_username(username)
        if user.is_2fa_enabled:
            return jsonify({"message": "Two-factor authentication required"}), 206
        login_user(user)
        return jsonify({"message": "Login successful"}), 200

    return jsonify({"message": "Invalid credentials"}), 401

@authentication_controller.route('/verify-2fa', methods=['POST'])
def verify_2fa():
    data = request.get_json()
    otp = data.get('otp')

    if not otp:
        return jsonify({"message": "OTP is required"}), 400

    user: User = current_user
    if AuthenticationService.verify_2fa(user.id, otp):
        login_user(user)
        return jsonify({"message": "Login successful"}), 200

    return jsonify({"message": "Invalid OTP"}), 401

@authentication_controller.route('/enable-2fa', methods=['POST'])
def enable_2fa():
    user: User = current_user
    AuthenticationService.enable_2fa(user.id)
    return jsonify({"message": "Two-factor authentication enabled"}), 200


# File 7: Update Main App to Register Authentication Controller in app.py