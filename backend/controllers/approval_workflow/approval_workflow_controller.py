# Epic Title: Account Opening and Service Modifications

from flask import Blueprint, jsonify, request
from flask_login import login_required, current_user
from backend.services.approval_workflow.approval_workflow_service import ApprovalWorkflowService

approval_workflow_controller = Blueprint('approval_workflow_controller', __name__)

@approval_workflow_controller.route('/approval-workflow/requests', methods=['POST'])
@login_required
def submit_request():
    data = request.get_json()
    request_id = data.get('request_id')
    request_type = data.get('request_type')

    if not request_id or not request_type:
        return jsonify({'message': 'Request ID and request type are required'}), 400

    workflow = ApprovalWorkflowService.submit_request(request_id, request_type)
    return jsonify({
        'id': workflow.id,
        'request_id': workflow.request_id,
        'request_type': workflow.request_type,
        'submitted_date': workflow.submitted_date,
        'approval_status': workflow.approval_status,
        'approved_by': workflow.approved_by,
        'processed_date': workflow.processed_date
    }), 201

@approval_workflow_controller.route('/approval-workflow/requests/<int:request_id>/approve', methods=['PUT'])
@login_required
def approve_request(request_id: int):
    ApprovalWorkflowService.approve_request(request_id, current_user.id)
    return jsonify({'message': 'Request approved successfully'}), 200

@approval_workflow_controller.route('/approval-workflow/requests/<int:request_id>/reject', methods=['PUT'])
@login_required
def reject_request(request_id: int):
    ApprovalWorkflowService.reject_request(request_id, current_user.id)
    return jsonify({'message': 'Request rejected successfully'}), 200

# File 5: Register Approval Workflow Controller Blueprint in app.py (Already Exists, Modified)