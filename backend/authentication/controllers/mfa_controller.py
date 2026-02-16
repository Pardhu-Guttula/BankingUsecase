# Epic Title: User Authentication and Security

from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required, get_jwt_identity
from backend.authentication.models import User
from backend.authentication.services.mfa_service import MFAService
from flask_sqlalchemy import SQLAlchemy

mfa_blueprint = Blueprint('mfa', __name__)
db = None  # Placeholder for SQLAlchemy instance
mfa_service = None  # Placeholder for MFAService instance

@mfa_blueprint.route('/mfa/setup', methods=['POST'])
@jwt_required()
def setup_mfa():
    current_user_id = get_jwt_identity()
    user = User.query.get_or_404(current_user_id)

    if user.mfa_enabled:
        return jsonify({"error": "MFA is already enabled."}), 400

    secret = mfa_service.setup_totp(user)
    return jsonify({"message": "MFA setup successfully.", "secret": secret}), 200

@mfa_blueprint.route('/mfa/disable', methods=['POST'])
@jwt_required()
def disable_mfa():
    current_user_id = get_jwt_identity()
    user = User.query.get_or_404(current_user_id)

    if not user.mfa_enabled:
        return jsonify({"error": "MFA is not enabled."}), 400

    mfa_service.disable_totp(user)
    return jsonify({"message": "MFA disabled successfully."}), 200

@mfa_blueprint.route('/mfa/verify', methods=['POST'])
@jwt_required()
def verify_mfa():
    current_user_id = get_jwt_identity()
    user = User.query.get_or_404(current_user_id)
    token = request.json.get('token')

    if mfa_service.validate_totp(user, token):
        return jsonify({"message": "MFA verification successful."}), 200
    else:
        return jsonify({"message": "MFA verification failed."}), 400