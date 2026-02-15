# Epic Title: Interaction History and Documentation Upload

from flask import Blueprint, request, jsonify
from flask_login import login_required, current_user
from backend.account.services.incomplete_application_service import IncompleteApplicationService

application_controller = Blueprint('application_controller', __name__)

@application_controller.route('/applications/incomplete', methods=['POST'])
@login_required
def save_application():
    data = request.get_json()
    application_data = data.get('application_data')
    if IncompleteApplicationService.save_application(current_user.id, application_data):
        return jsonify({"message": "Application saved successfully."}), 201
    return jsonify({"message": "Failed to save application."}), 500

@application_controller.route('/applications/incomplete', methods=['GET'])
@login_required
def get_incomplete_application():
    application = IncompleteApplicationService.get_incomplete_application(current_user.id)
    if application:
        return jsonify({
            "id": application.id,
            "application_data": application.application_data,
            "saved_at": application.saved_at.strftime("%Y-%m-%d %H:%M:%S")
        })
    return jsonify({"message": "No incomplete application found."}), 404


# File 5: Update Main App to Register Application Controller in app.py