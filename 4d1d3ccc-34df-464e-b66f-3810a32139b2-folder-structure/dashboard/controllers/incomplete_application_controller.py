# Epic Title: Interaction History and Documentation Upload

from flask import Blueprint, request, jsonify
from flask_login import login_required, current_user
from dashboard.services.incomplete_application_service import IncompleteApplicationService

incomplete_application_controller = Blueprint('incomplete_application_controller', __name__)

@incomplete_application_controller.route('/applications/save', methods=['POST'])
@login_required
def save_application():
    data = request.json
    application_data = data.get('application_data')

    if not application_data:
        return jsonify({"error": "Application data is required"}), 400

    application = IncompleteApplicationService.save_incomplete_application(current_user.id, application_data)
    return jsonify({
        "id": application.id,
        "application_data": application.application_data,
        "saved_at": application.saved_at
    }), 201

@incomplete_application_controller.route('/applications/resume', methods=['GET'])
@login_required
def get_saved_application():
    application = IncompleteApplicationService.get_incomplete_application(current_user.id)
    return jsonify(application), 200


# File 5: App Update to Register Incomplete Application Controller in app.py