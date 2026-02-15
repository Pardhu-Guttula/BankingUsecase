# Epic Title: User Authentication and Security

from flask import Blueprint, request, jsonify, session
from flask_login import login_required, logout_user, login_user
from backend.services.authentication.authentication_service import AuthenticationService

authentication_controller = Blueprint('authentication_controller', __name__)

@authentication_controller.route('/login', methods=['POST'])
def login():
    data = request.json
    username = data.get('username')
    password = data.get('password')

    authentication_result = AuthenticationService.authenticate(username, password)
    if authentication_result == "mfa_required":
        session['username'] = username
        return jsonify({"mfa_required": True}), 200
    elif authentication_result:
        return jsonify({"message": "Login successful"}), 200
    else:
        return jsonify({"error": "Invalid username or password"}), 401

@authentication_controller.route('/verify-mfa', methods=['POST'])
def verify_mfa():
    data = request.json
    token = data.get('token')
    username = session.get('username')

    if not username or not token:
        return jsonify({"error": "Invalid request"}), 400

    if AuthenticationService.verify_mfa(username, token):
        session.pop('username', None)
        return jsonify({"message": "Login successful"}), 200
    else:
        return jsonify({"error": "Invalid MFA token"}), 401

@authentication_controller.route('/logout', methods=['POST'])
@login_required
def logout():
    logout_user()
    return jsonify({"message": "Logout successful"}), 200

@authentication_controller.route('/setup-mfa', methods=['POST'])
@login_required
def setup_mfa():
    secret = AuthenticationService.setup_mfa(current_user.id)
    if secret:
        return jsonify({"mfa_secret": secret}), 200
    else:
        return jsonify({"error": "Failed to setup MFA"}), 500

@authentication_controller.route('/disable-mfa', methods=['POST'])
@login_required
def disable_mfa():
    AuthenticationService.disable_mfa(current_user.id)
    return jsonify({"message": "MFA disabled"}), 200


# File 5: App Update to Register Authentication Controller in app.py