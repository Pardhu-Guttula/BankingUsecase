# Epic Title: Account Opening and Service Modifications

from flask import Blueprint, request, jsonify
from flask_login import login_required, current_user
from backend.approval_workflow.services.approval_service import ApprovalService

approval_controller = Blueprint('approval_controller', __name__)

@approval_controller.route('/approve_request/<int:request_id>', methods=['POST'])
@login_required
def approve_request(request_id):
    if ApprovalService.approve_request(request_id):
        return jsonify({"message": "Request approved successfully."}), 200
    return jsonify({"message": "Failed to approve request."}), 500

@approval_controller.route('/reject_request/<int:request_id>', methods=['POST'])
@login_required
def reject_request(request_id):
    if ApprovalService.reject_request(request_id):
        return jsonify({"message": "Request rejected successfully."}), 200
    return jsonify({"message": "Failed to reject request."}), 500

@approval_controller.route('/process_request/<int:request_id>', methods=['POST'])
@login_required
def process_request(request_id):
    if ApprovalService.process_request(request_id):
        return jsonify({"message": "Request processed successfully."}), 200
    return jsonify({"message": "Failed to process request."}), 500


# File 5: Update Main App to Ensure Approval Workflow Initialization in app.py