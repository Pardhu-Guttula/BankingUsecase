# Epic Title: Service Modification Requests

from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from backend.account.service_modifications.services import ServiceModificationService

service_modification_blueprint = Blueprint('service_modifications', __name__)
service_modification_service = ServiceModificationService(db)

@service_modification_blueprint.route('/account/service_modifications', methods=['POST'])
@jwt_required()
def create_service_modification_request():
    current_user_id = get_jwt_identity()
    data = request.json
    service_type = data.get('service_type')
    new_value = data.get('new_value')
    
    if not service_type or not new_value:
        return jsonify({"error": "Service type and new value are required"}), 400

    modification_request = service_modification_service.create_modification_request(current_user_id, service_type, new_value)
    return jsonify({
        "request_id": modification_request.id,
        "service_type": modification_request.service_type,
        "new_value": modification_request.new_value,
        "status": modification_request.status,
        "created_at": modification_request.created_at
    }), 201

# Additional endpoint to approve a service modification request
@service_modification_blueprint.route('/account/service_modifications/<int:request_id>/approve', methods=['PATCH'])
@jwt_required()
def approve_service_modification_request(request_id: int):
    if service_modification_service.update_request_status(request_id, 'approved'):
        return jsonify({"status": "approved"}), 200
    return jsonify({"error": "Request not found or already processed"}), 404