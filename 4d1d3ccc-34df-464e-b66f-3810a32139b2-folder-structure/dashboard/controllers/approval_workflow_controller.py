# Epic Title: Approval and Processing Workflows

from flask import Blueprint, request, jsonify
from flask_login import login_required, current_user
from dashboard.services.approval_workflow_service import ApprovalWorkflowService

approval_workflow_controller = Blueprint('approval_workflow_controller', __name__)

@approval_workflow_controller.route('/approval-workflows', methods=['POST'])
@login_required
def create_approval_workflow():
    data = request.json
    request_type = data.get('request_type')
    request_id = data.get('request_id')
    approver_id = data.get('approver_id')

    if not request_type or not request_id or not approver_id:
        return jsonify({"error": "Request type, request ID, and approver ID are required"}), 400

    workflow = ApprovalWorkflowService.create_workflow(request_type, request_id, approver_id)
    return jsonify({
        "id": workflow.id,
        "request_type": workflow.request_type,
        "request_id": workflow.request_id,
        "approver_id": workflow.approver_id,
        "status": workflow.status,
        "created_at": workflow.created_at
    }), 201

@approval_workflow_controller.route('/approval-workflows/<int:workflow_id>/process', methods=['PUT'])
@login_required
def process_approval_workflow(workflow_id: int):
    data = request.json
    approved = data.get('approved', False)
    approver_id = current_user.id

    status = ApprovalWorkflowService.process_workflow("generic", workflow_id, approver_id, approved)
    if status == "Invalid request or approver":
        return jsonify({"error": status}), 400
    return jsonify({"message": f"Request {status} successfully"}), 200


# File 5: App Update to Register Approval Workflow Controller in app.py