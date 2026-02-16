# Epic Title: Account Opening and Service Modifications

from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required, get_jwt_identity
from backend.approval_workflow.services import ApprovalService

approval_workflow_blueprint = Blueprint('approval_workflow', __name__)
# Initialize ApprovalService later in app.py to inject dependencies
approval_service = None  # Placeholder for real instance

@approval_workflow_blueprint.route('/approval/initiate', methods=['POST'])
@jwt_required()
def initiate_approval():
    data = request.json
    request_type = data.get('request_type')
    request_id = data.get('request_id')
    
    if not request_type or not request_id:
        return jsonify({"error": "Request type and request ID are required"}), 400

    approval_request = approval_service.initiate_approval(request_type, request_id)
    return jsonify({
        "message": "Approval request initiated successfully",
        "approval_request": {
            "id": approval_request.id,
            "request_type": approval_request.request_type,
            "request_id": approval_request.request_id,
            "status": approval_request.status,
            "created_at": approval_request.created_at
        }
    }), 201

@approval_workflow_blueprint.route('/approval/approve/<int:approval_request_id>', methods=['POST'])
@jwt_required()
def approve_request(approval_request_id: int):
    try:
        approval_service.approve_request(approval_request_id)
        return jsonify({"message": "Request approved successfully"}), 200
    except ValueError as e:
        return jsonify({"error": str(e)}), 400