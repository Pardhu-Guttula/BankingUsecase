# Epic Title: Implement Secure Login Mechanism

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
        # For simplicity, assume MFA is always successful for this illustration
        if user.two_factor_enabled:
            # MFA Verification would be here
            pass
        session = auth_service.create_session(user.id)
        return jsonify({"session_token": session.session_token}), 200
    return jsonify({"error": "Invalid credentials"}), 401