# Epic Title: Account Opening and Service Modifications

from flask import Blueprint, jsonify, request
from flask_login import login_required, current_user
from backend.services.approval_workflow.approval_service import ApprovalService

approval_controller = Blueprint('approval_controller', __name__)

@approval_controller.route('/approvals/pending', methods=['GET'])
@login_required
def get_pending_approvals():
    pending_approvals = ApprovalService.get_pending_approvals()
    return jsonify([{
        "id": approval.id,
        "request_id": approval.request_id,
        "request_type": approval.request_type,
        "status": approval.status,
        "timestamp": approval.timestamp,
        "approver_id": approval.approver_id,
    } for approval in pending_approvals]), 200

@approval_controller.route('/approvals/approve/<int:approval_id>', methods=['POST'])
@login_required
def approve_request(approval_id: int):
    ApprovalService.approve(approval_id, current_user.id)
    return jsonify({"message": "Request approved successfully"}), 200


# File 6: Service Integration for Account Opening and Modifications in account/services/opening/account_opening_service.py (Update)