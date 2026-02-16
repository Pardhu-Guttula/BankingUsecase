# Epic Title: Interaction History and Documentation Upload

from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required, get_jwt_identity
from backend.applications.services import ApplicationService

applications_blueprint = Blueprint('applications', __name__)
# Initialize ApplicationService later in app.py to inject dependencies
application_service = None  # Placeholder for real instance

@applications_blueprint.route('/applications/save', methods=['POST'])
@jwt_required()
def save_application():
    current_user_id = get_jwt_identity()
    data = request.json.get('data')
    if not data:
        return jsonify({"error": "No application data provided"}), 400

    application = application_service.save_incomplete_application(current_user_id, data)
    return jsonify({"message": "Application saved successfully", "application_id": application.id}), 201

@applications_blueprint.route('/applications/incomplete', methods=['GET'])
@jwt_required()
def get_incomplete_application():
    current_user_id = get_jwt_identity()
    application = application_service.get_incomplete_application(current_user_id)
    if application:
        return jsonify({
            "id": application.id,
            "data": application.data,
            "saved_at": application.saved_at
        }), 200
    return jsonify({"message": "No incomplete application found"}), 404