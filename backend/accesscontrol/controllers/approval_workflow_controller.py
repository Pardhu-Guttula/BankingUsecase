# Epic Title: Approval and Processing Workflows

from flask import Blueprint, request, jsonify
from ..services.approval_workflow_service import ApprovalWorkflowService

approval_workflow_controller = Blueprint('approval_workflow_controller', __name__)
approval_workflow_service = ApprovalWorkflowService()

@approval_workflow_controller.route('/approval_workflows', methods=['GET'])
def get_pending_requests():
    pending_requests = approval_workflow_service.pending_requests()
    return jsonify(pending_requests), 200

@approval_workflow_controller.route('/approval_workflows/<int:workflow_id>/approve', methods=['POST'])
def approve_request(workflow_id):
    approver = request.json.get('approver')
    if approval_workflow_service.approve_request(workflow_id, approver):
        return jsonify({"message": "Request approved successfully"}), 200
    return jsonify({"error": "Failed to approve request"}), 500

@approval_workflow_controller.route('/approval_workflows/<int:workflow_id>/reject', methods=['POST'])
def reject_request(workflow_id):
    approver = request.json.get('approver')
    if approval_workflow_service.reject_request(workflow_id, approver):
        return jsonify({"message": "Request rejected successfully"}), 200
    return jsonify({"error": "Failed to reject request"}), 500


# File 6: Database Schema for ApprovalWorkflow in database/approval_workflows.sql