# Epic Title: Real-time Status Updates and Notifications

from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required, get_jwt_identity
from backend.status.services import StatusService

status_blueprint = Blueprint('status', __name__)
# Initialize EmailService and StatusService later in app.py to inject dependencies
status_service = None  # Placeholder for real instance

@status_blueprint.route('/status/<int:request_id>', methods=['GET'])
@jwt_required()
def get_status(request_id: int):
    current_user_id = get_jwt_identity()
    status = status_service.get_status(request_id)
    if status and status.user_id == current_user_id:
        return jsonify({
            "request_id": status.request_id,
            "status": status.status,
            "updated_at": status.updated_at
        }), 200
    return jsonify({"error": "Status not found or unauthorized access"}), 404