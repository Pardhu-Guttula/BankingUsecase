# Epic Title: Interaction History and Documentation Upload

from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from backend.applications.services.application_service import ApplicationService

application_blueprint = Blueprint('applications', __name__)
application_service = ApplicationService()

@application_blueprint.route('/save-progress', methods=['POST'])
@jwt_required()
def save_progress():
    form_data = request.json.get('form_data')
    if not form_data:
        return jsonify({"error": "No form data provided"}), 400

    user_id = get_jwt_identity()
    application = application_service.save_application_progress(user_id, form_data)
    return jsonify({
        "id": application.id,
        "user_id": application.user_id,
        "form_data": application.form_data,
        "saved_at": application.saved_at
    }), 201

@application_blueprint.route('/retrieve-progress', methods=['GET'])
@jwt_required()
def retrieve_progress():
    user_id = get_jwt_identity()
    applications = application_service.get_application_progress(user_id)
    return jsonify([{
        "id": app.id,
        "user_id": app.user_id,
        "form_data": app.form_data,
        "saved_at": app.saved_at
    } for app in applications]), 200

@application_blueprint.route('/delete-progress/<int:application_id>', methods=['DELETE'])
@jwt_required()
def delete_progress(application_id: int):
    application_service.delete_application_progress(application_id)
    return '', 204