# Epic Title: Manage Secure Storage of Credentials

from flask import Blueprint, request, jsonify
from flask_login import login_required, logout_user, current_user
from authentication.services.authentication_service import AuthenticationService

authentication_controller = Blueprint('authentication_controller', __name__)

@authentication_controller.route('/login', methods=['POST'])
def login():
    data = request.json
    username = data.get('username')
    password = data.get('password')

    if not username or not password:
        return jsonify({"error": "Username and password are required"}), 400

    user = AuthenticationService.authenticate(username, password)
    if user:
        return jsonify({"message": "Login successful"}), 200
    else:
        return jsonify({"error": "Invalid username or password"}), 401

@authentication_controller.route('/register', methods=['POST'])
def register():
    data = request.json
    username = data.get('username')
    password = data.get('password')
    email = data.get('email')
    phone_number = data.get('phone_number')
    two_factor_enabled = data.get('two_factor_enabled', False)

    if not username or not password or not email or not phone_number:
        return jsonify({"error": "All fields are required"}), 400

    user = AuthenticationService.register(username, password, email, phone_number, two_factor_enabled)
    return jsonify({"message": "User registered successfully", "user_id": user.id}), 201

@authentication_controller.route('/logout', methods=['POST'])
@login_required
def logout():
    logout_user()
    return jsonify({"message": "Logged out successfully"}), 200


# File 6: App Update to Register Authentication Controller in app.py