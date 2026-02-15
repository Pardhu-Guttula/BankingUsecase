# Epic Title: Interaction History and Documentation Upload

from flask import Blueprint, request, jsonify
from flask_login import login_required, current_user
from backend.services.account.incomplete_application_service import IncompleteApplicationService

incomplete_application_controller = Blueprint('incomplete_application_controller', __name__)

@incomplete_application_controller.route('/applications/save', methods=['POST'])
@login_required
def save_application():
    data = request.json.get('data')
    if not data:
        return jsonify({"message": "No application data provided"}), 400

    application = IncompleteApplicationService.save_application(current_user.id, data)
    return jsonify({"message": "Application saved successfully", "application_id": application.id}), 201

@incomplete_application_controller.route('/applications/update/<int:application_id>', methods=['POST'])
@login_required
def update_application(application_id: int):
    data = request.json.get('data')
    if not data:
        return jsonify({"message": "No application data provided"}), 400

    application = IncompleteApplicationService.update_application(application_id, data)
    return jsonify({"message": "Application updated successfully"}), 200

@incomplete_application_controller.route('/applications/view', methods=['GET'])
@login_required
def view_applications():
    applications = IncompleteApplicationService.get_user_applications(current_user.id)
    applications_data = [{
        "id": app.id,
        "data": app.data,
        "last_updated": app.last_updated
    } for app in applications]
    return jsonify(applications_data), 200


# File 6: Update Main App to Register Incomplete Application Controller in app.py