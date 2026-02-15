# Epic Title: Approval and Processing Workflows

from flask import Blueprint, request, jsonify
from flask_login import login_required, current_user
from backend.services.approval_workflow.approval_workflow_service import ApprovalWorkflowService

approval_workflow_controller = Blueprint('approval_workflow_controller', __name__)

@approval_workflow_controller.route('/approval/workflows', methods=['POST'])
@login_required
def create_approval_workflow():
    data = request.get_json()
    request_id = data.get('request_id')
    request_type = data.get('request_type')
    approver_id = data.get('approver_id')

    if not request_id or not request_type or not approver_id:
        return jsonify({'message': 'Request ID, request type, and approver ID are required'}), 400

    ApprovalWorkflowService.create_workflow(request_id, request_type, approver_id)
    return jsonify({'message': 'Approval workflow created successfully'}), 201

@approval_workflow_controller.route('/approval/workflows/<int:workflow_id>/approve', methods=['POST'])
@login_required
def approve_approval_workflow(workflow_id: int):
    data = request.get_json()
    comments = data.get('comments', '')

    ApprovalWorkflowService.approve_workflow(workflow_id, comments)
    return jsonify({'message': 'Workflow approved successfully'}), 200

@approval_workflow_controller.route('/approval/workflows/<int:workflow_id>/reject', methods=['POST'])
@login_required
def reject_approval_workflow(workflow_id: int):
    data = request.get_json()
    comments = data.get('comments', '')

    ApprovalWorkflowService.reject_workflow(workflow_id, comments)
    return jsonify({'message': 'Workflow rejected successfully'}), 200

@approval_workflow_controller.route('/approval/workflows', methods=['GET'])
@login_required
def get_approval_workflows():
    request_id = request.args.get('request_id')
    request_type = request.args.get('request_type')

    if not request_id or not request_type:
        return jsonify({'message': 'Request ID and request type are required'}), 400

    workflows = ApprovalWorkflowService.get_workflows_by_request(request_id, request_type)
    return jsonify({'workflows': [workflow.serialize() for workflow in workflows]}), 200


# File 5: Schema for Approval Workflows Table in database/create_approval_workflows_table.sql