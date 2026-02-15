# Epic Title: Save and Resume Incomplete Applications

from flask import Blueprint, request, jsonify
from flask_login import login_required, current_user
from backend.interaction_history.services.application_service.py import ApplicationService

application_controller = Blueprint('application_controller', __name__)

@application_controller.route('/save_application', methods=['POST'])
@login_required
def save_application():
    data = request.json.get('data')
    if not data:
        return jsonify({"error": "Application data is required"}), 400

    ApplicationService.save_application(current_user.id, data)
    return jsonify({"message": "Application saved successfully"}), 200

@application_controller.route('/resume_application/<int:app_id>', methods=['GET'])
@login_required
def resume_application(app_id):
    application = ApplicationService.resume_application(app_id)
    if application.user_id != current_user.id:
        return jsonify({"error": "Unauthorized access"}), 403

    return jsonify({"id": application.id, "data": application.data, "status": application.status})


# File 5: Save and Resume Application Template in user_dashboard/templates/application.html