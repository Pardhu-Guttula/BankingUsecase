# Epic Title: Account Opening and Service Modifications

from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required, get_jwt_identity
from backend.account.services.service_modification_service import ServiceModificationService

service_modification_blueprint = Blueprint('service_modification', __name__)
# Initialize ServiceModificationService later in app.py to inject dependencies
service_modification_service = None  # Placeholder for real instance

@service_modification_blueprint.route('/accounts/service_modifications', methods=['POST'])
@jwt_required()
def create_modification_request():
    current_user_id = get_jwt_identity()
    account_id = request.json.get('account_id')
    service_name = request.json.get('service_name')
    new_value = request.json.get('new_value')

    if not account_id or not service_name or not new_value:
        return jsonify({"error": "All fields (account_id, service_name, new_value) are required"}), 400

    modification_request = service_modification_service.create_modification_request(current_user_id, account_id, service_name, new_value)
    return jsonify({
        "message": "Service modification request created successfully",
        "modification_request": {
            "id": modification_request.id,
            "account_id": modification_request.account_id,
            "service_name": modification_request.service_name,
            "new_value": modification_request.new_value,
            "status": modification_request.status,
            "created_at": modification_request.created_at
        }
    }), 201

@service_modification_blueprint.route('/accounts/service_modifications', methods=['GET'])
@jwt_required()
def get_modification_requests():
    current_user_id = get_jwt_identity()
    modification_requests = service_modification_service.get_modification_requests_for_user(current_user_id)
    return jsonify([{
        "id": req.id,
        "account_id": req.account_id,
        "service_name": req.service_name,
        "new_value": req.new_value,
        "status": req.status,
        "created_at": req.created_at
    } for req in modification_requests]), 200