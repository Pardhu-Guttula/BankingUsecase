# Epic Title: Account Opening and Service Modifications

from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required, current_user
from backend.services.approval_workflow.approval_service import ApprovalService
from backend.forms.service_modification_form import ServiceModificationForm

approval_controller = Blueprint('approval_controller', __name__)

@approval_controller.route('/submit_request/<request_type>/<int:request_id>', methods=['POST'])
@login_required
def submit_request(request_type, request_id):
    result = ApprovalService.submit_approval_request(current_user.id, request_type, request_id)
    if result:
        flash('Request submitted successfully for approval.', 'success')
    else:
        flash('An error occurred while submitting your request.', 'danger')
    return redirect(url_for('dashboard_controller.dashboard'))

@approval_controller.route('/process_request/<int:approval_request_id>/<status>', methods=['POST'])
@login_required
def process_request(approval_request_id, status):
    result = ApprovalService.process_approval_request(approval_request_id, status)
    if result:
        flash('Approval request processed successfully.', 'success')
    else:
        flash('An error occurred while processing the approval request.', 'danger')
    return redirect(url_for('dashboard_controller.dashboard'))


# File 5: Update Account Service to Include Approval Workflows in account/services/account_service.py