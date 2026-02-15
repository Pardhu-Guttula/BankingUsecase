# Epic Title: Core Banking System Integration

from flask import Blueprint, request, jsonify
from flask_login import login_required, current_user
from backend.integration.services.api_service import APIService

api_controller = Blueprint('api_controller', __name__)

@api_controller.route('/generate-token', methods=['POST'])
@login_required
def generate_token():
    token = APIService.generate_token()
    return jsonify({"token": token}), 201

@api_controller.route('/secure-endpoint', methods=['POST'])
def secure_endpoint():
    token = request.headers.get('Authorization')
    if not token or not APIService.validate_token(token):
        return jsonify({"message": "Unauthorized"}), 401

    # Process the secure API request
    return jsonify({"message": "Secure data processed successfully"}), 200


# File 5: Update Main App to Register API Controller and Configure Middleware in app.py