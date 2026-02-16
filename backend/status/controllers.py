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

@status_blueprint.route('/notifications', methods=['GET'])
@jwt_required()
def get_notifications():
    current_user_id = get_jwt_identity()
    notifications = status_service.get_notifications(current_user_id)
    return jsonify([{
        "id": n.id,
        "message": n.message,
        "created_at": n.created_at,
        "is_read": n.is_read
    } for n in notifications]), 200

@status_blueprint.route('/notifications/<int:notification_id>/read', methods=['POST'])
@jwt_required()
def mark_notification_as_read(notification_id: int):
    status_service.mark_notification_as_read(notification_id)
    return jsonify({"success": True}), 200