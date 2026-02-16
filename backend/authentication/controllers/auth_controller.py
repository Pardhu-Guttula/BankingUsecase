# Epic Title: User Authentication and Security

from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token
from backend.authentication.models import User
from backend.authentication.services.mfa_service import MFAService
from flask_sqlalchemy import SQLAlchemy

auth_blueprint = Blueprint('auth', __name__)
db = None  # Placeholder for SQLAlchemy instance
mfa_service = None  # Placeholder for MFAService instance

@auth_blueprint.route('/login', methods=['POST'])
def login():
    username = request.json.get('username')
    password = request.json.get('password')

    user = User.query.filter_by(username=username).first()
    if user and user.check_password(password):
        if user.mfa_enabled:
            return jsonify({"message": "MFA required", "mfa_required": True}), 200
        access_token = create_access_token(identity=user.id)
        return jsonify(access_token=access_token), 200
    else:
        return jsonify({"error": "Invalid username or password"}), 401

@auth_blueprint.route('/login/mfa', methods=['POST'])
def login_mfa():
    username = request.json.get('username')
    password = request.json.get('password')
    token = request.json.get('token')

    user = User.query.filter_by(username=username).first()
    if user and user.check_password(password):
        if user.mfa_enabled and mfa_service.validate_totp(user, token):
            access_token = create_access_token(identity=user.id)
            return jsonify(access_token=access_token), 200
        return jsonify({"error": "Invalid MFA token"}), 401
    else:
        return jsonify({"error": "Invalid username or password"}), 401