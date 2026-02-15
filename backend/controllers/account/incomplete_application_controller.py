# Epic Title: Interaction History and Documentation Upload

from flask import Blueprint, request, jsonify
from flask_login import login_required, current_user
from backend.services.account.incomplete_application_service import IncompleteApplicationService

incomplete_application_controller = Blueprint('incomplete_application_controller', __name__)

@incomplete_application_controller.route('/incomplete_applications', methods=['POST'])
@login_required
def save_application():
    form_data = request.json.get('form_data')
    if not form_data:
        return jsonify({'message': 'Form data is required'}), 400

    application = IncompleteApplicationService.save_application(current_user.id, form_data)
    return jsonify({
        'id': application.id,
        'user_id': application.user_id,
        'form_data': application.form_data,
        'saved_at': application.saved_at
    })

@incomplete_application_controller.route('/incomplete_applications', methods=['GET'])
@login_required
def get_user_applications():
    applications = IncompleteApplicationService.get_user_applications(current_user.id)
    applications_list = [{
        'id': app.id,
        'user_id': app.user_id,
        'form_data': app.form_data,
        'saved_at': app.saved_at
    } for app in applications]
    return jsonify(applications_list)

# File 5: Register Incomplete Application Controller Blueprint in app.py (Already Exists, Modified)