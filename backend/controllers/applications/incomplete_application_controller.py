# Epic Title: Save and Resume Incomplete Applications

from flask import Blueprint, request, jsonify
from flask_login import login_required, current_user
from backend.services.applications.incomplete_application_service import IncompleteApplicationService

incomplete_application_controller = Blueprint('incomplete_application_controller', __name__)

@incomplete_application_controller.route('/applications/incomplete', methods=['POST'])
@login_required
def save_incomplete_application():
    data = request.get_json()
    application_data = data.get('application_data')

    if not application_data:
        return jsonify({'message': 'Application data is required'}), 400

    try:
        IncompleteApplicationService.save_application(current_user.id, application_data)
        return jsonify({'message': 'Application saved successfully'}), 201
    except Exception as e:
        return jsonify({'message': str(e)}), 500

@incomplete_application_controller.route('/applications/incomplete', methods=['PUT'])
@login_required
def update_incomplete_application():
    data = request.get_json()
    application_data = data.get('application_data')

    if not application_data:
        return jsonify({'message': 'Application data is required'}), 400

    try:
        IncompleteApplicationService.update_application(current_user.id, application_data)
        return jsonify({'message': 'Application updated successfully'}), 200
    except Exception as e:
        return jsonify({'message': str(e)}), 500

@incomplete_application_controller.route('/applications/incomplete', methods=['GET'])
@login_required
def get_incomplete_application():
    try:
        application = IncompleteApplicationService.get_application(current_user.id)
        if application:
            return jsonify({'application_data': application.application_data}), 200
        else:
            return jsonify({'message': 'No incomplete application found'}), 404
    except Exception as e:
        return jsonify({'message': str(e)}), 500


# File 5: Schema for Incomplete Applications Table in `database/create_incomplete_applications_table.sql`