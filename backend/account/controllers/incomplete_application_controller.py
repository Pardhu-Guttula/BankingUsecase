# Epic Title: Interaction History and Documentation Upload

from flask import Blueprint, jsonify, request
from flask_login import login_required, current_user
from backend.services.account.incomplete_application_service import IncompleteApplicationService

incomplete_application_controller = Blueprint('incomplete_application_controller', __name__)

@incomplete_application_controller.route('/applications/incomplete', methods=['POST'])
@login_required
def save_incomplete_application():
    application_data = request.json.get('application_data')
    if not application_data:
        return jsonify({'message': 'No application data provided'}), 400

    incomplete_application = IncompleteApplicationService.save_incomplete_application(current_user.id, application_data)
    return jsonify({
        'id': incomplete_application.id,
        'user_id': incomplete_application.user_id,
        'application_data': incomplete_application.application_data,
        'saved_at': incomplete_application.saved_at
    }), 201

@incomplete_application_controller.route('/applications/incomplete', methods=['GET'])
@login_required
def get_incomplete_application():
    incomplete_application = IncompleteApplicationService.get_incomplete_application(current_user.id)
    if incomplete_application:
        return jsonify({
            'id': incomplete_application.id,
            'user_id': incomplete_application.user_id,
            'application_data': incomplete_application.application_data,
            'saved_at': incomplete_application.saved_at
        })
    return jsonify({'message': 'No incomplete application found'}), 404


# File 5: Update Main App to Register Incomplete Application Controller Blueprint in app.py (Already Exists, Modified)