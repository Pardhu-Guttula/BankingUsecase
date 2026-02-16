# Epic Title: Approval and Processing Workflows

from flask import Blueprint, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from backend.approval_workflow.services import ApprovalService

approval_workflow_blueprint = Blueprint('approval_workflow', __name__)
approval_service = ApprovalService(db)

@approval_workflow_blueprint.route('/approval_workflow/<int:request_id>/<string:request_type>', methods=['GET'])
@jwt_required()
def get_approval_status(request_id: int, request_type: str):
    workflow = approval_service.get_approval_status(request_id, request_type)
    if workflow:
        return jsonify({
            "workflow_id": workflow.id,
            "request_id": workflow.request_id,
            "request_type": workflow.request_type,
            "status": workflow.status,
            "processed_at": workflow.processed_at,
            "created_at": workflow.created_at
        }), 200
    return jsonify({"error": "Workflow not found"}), 404

@approval_workflow_blueprint.route('/approval_workflow/<int:workflow_id>/approve', methods=['PATCH'])
@jwt_required()
def approve_request(workflow_id: int):
    if approval_service.update_approval_status(workflow_id, 'approved'):
        return jsonify({"status": "approved"}), 200
    return jsonify({"error": "Workflow not found"}), 404