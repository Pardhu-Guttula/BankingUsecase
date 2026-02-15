# Epic Title: Interaction History and Documentation Upload

from flask import Blueprint, jsonify, request
from flask_login import login_required, current_user
from backend.services.account.incomplete_application_service import IncompleteApplicationService

incomplete_application_controller = Blueprint('incomplete_application_controller', __name__)

@incomplete_application_controller.route('/applications/incomplete', methods=['POST'])
@login_required
def save_incomplete_application():
    data = request.get_json()
    status = data.get('status')
    application_data = data.get('application_data')
    if not status or not application_data:
        return jsonify({'message': 'Status and application data are required'}), 400

    user_id = current_user.id
    application = IncompleteApplicationService.save_incomplete_application(user_id, status, application_data)
    return jsonify({
        'id': application.id,
        'status': application.status,
        'application_data': application.application_data,
        'saved_at': application.saved_at
    }), 201

@incomplete_application_controller.route('/applications/incomplete', methods=['GET'])
@login_required
def get_user_incomplete_applications():
    user_id = current_user.id
    applications = IncompleteApplicationService.get_incomplete_applications(user_id)
    applications_list = [{
        'id': application.id,
        'status': application.status,
        'application_data': application.application_data,
        'saved_at': application.saved_at
    } for application in applications]
    return jsonify(applications_list)

@incomplete_application_controller.route('/applications/incomplete/<int:application_id>', methods=['GET'])
@login_required
def get_incomplete_application(application_id: int):
    application = IncompleteApplicationService.get_incomplete_application_by_id(application_id)
    if not application:
        return jsonify({'message': 'Application not found'}), 404

    return jsonify({
        'id': application.id,
        'status': application.status,
        'application_data': application.application_data,
        'saved_at': application.saved_at
    })

# File 5: Register Incomplete Application Controller Blueprint in app.py (Already Exists, Modified)