# Epic Title: Implement Secure Login Mechanism

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

    user_id = AuthenticationService.authenticate(username, password)
    if user_id:
        return jsonify({"message": "Two-factor code sent", "user_id": user_id}), 200
    elif user_id is None:
        return jsonify({"message": "Login successful"}), 200
    else:
        return jsonify({"error": "Invalid username or password"}), 401

@authentication_controller.route('/verify', methods=['POST'])
def verify_two_factor():
    data = request.json
    user_id = data.get('user_id')
    code = data.get('code')

    if not user_id or not code:
        return jsonify({"error": "User ID and code are required"}), 400

    if AuthenticationService.verify_two_factor(user_id, code):
        return jsonify({"message": "Login successful"}), 200
    else:
        return jsonify({"error": "Invalid two-factor code"}), 401

@authentication_controller.route('/logout', methods=['POST'])
@login_required
def logout():
    logout_user()
    return jsonify({"message": "Logged out successfully"}), 200


# File 8: App Update to Register Authentication Controller in app.py