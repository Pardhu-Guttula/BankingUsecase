# Epic Title: User Authentication and Security

from flask import Blueprint, request, jsonify
from flask_login import login_user, logout_user, login_required
from backend.models.user_model import User
from backend.services.authentication.authentication_service import AuthenticationService

authentication_controller = Blueprint('authentication_controller', __name__)

@authentication_controller.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    token = data.get('token')

    user = User.query.filter_by(username=username).first()

    if user and AuthenticationService.authenticate_user(user.id, password, token):
        login_user(user)
        return jsonify({'message': 'Login successful'}), 200

    return jsonify({'message': 'Invalid credentials or token'}), 401

@authentication_controller.route('/logout', methods=['POST'])
@login_required
def logout():
    logout_user()
    return jsonify({'message': 'Logout successful'}), 200

@authentication_controller.route('/register/mfa', methods=['POST'])
@login_required
def register_mfa():
    mfa_secret = AuthenticationService.register_mfa(current_user.id)
    return jsonify({'mfa_secret': mfa_secret}), 200

# File 5: Register Authentication Controller Blueprint in app.py (Already Exists, Modified)