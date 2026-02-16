# Epic Title: Manage Secure Storage of Credentials

from flask import Blueprint, request, jsonify
from backend.authentication.services.authentication_service import AuthenticationService

auth_routes = Blueprint('auth_routes', __name__)
auth_service = AuthenticationService(db)

@auth_routes.route('/login', methods=['POST'])
def login():
    data = request.json
    username = data.get('username')
    password = data.get('password')
    user = auth_service.authenticate_user(username, password)
    if user:
        if user.two_factor_enabled:
            # MFA Verification would be implemented here
            pass
        session = auth_service.create_session(user.id)
        return jsonify({"session_token": session.session_token}), 200
    return jsonify({"error": "Invalid credentials"}), 401

@auth_routes.route('/check-session', methods=['POST'])
def check_session():
    data = request.json
    session_token = data.get('session_token')
    if auth_service.is_session_valid(session_token):
        auth_service.update_last_activity(session_token)
        return jsonify({"status": "active"}), 200
    return jsonify({"status": "expired"}), 401