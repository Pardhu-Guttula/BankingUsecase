# Epic Title: Real-time Status Updates and Notifications

from flask import Blueprint, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from flask_socketio import emit
from backend.status.models.request_status import RequestStatus, db
from backend.status.services.email_service import EmailService
from backend.status.services.notification_service import NotificationService

status_blueprint = Blueprint('status', __name__)
email_service = None  # Will be initialized in app.py
notification_service = None  # Will be initialized in app.py

@status_blueprint.route('/status/<int:request_id>', methods=['GET'])
@jwt_required()
def get_status(request_id: int):
    status = RequestStatus.query.filter_by(request_id=request_id).order_by(RequestStatus.updated_at.desc()).first()
    if status:
        return jsonify({
            "request_id": status.request_id,
            "status": status.status,
            "updated_at": status.updated_at
        }), 200
    else:
        return jsonify({
            "error": "Request status not found"
        }), 404

@status_blueprint.route('/notifications', methods=['GET'])
@jwt_required()
def get_notifications():
    user_id = get_jwt_identity()
    notifications = notification_service.get_unread_notifications(user_id)
    return jsonify([{
        "id": n.id,
        "message": n.message,
        "created_at": n.created_at
    } for n in notifications]), 200

def emit_status_update(request_id: int, status: str, user_email: str, user_id: int) -> None:
    new_status = RequestStatus(request_id=request_id, status=status)
    db.session.add(new_status)
    db.session.commit()

    notification_message = f"Your request with ID {request_id} has been updated to: {status}"
    notification_service.create_notification(user_id, notification_message)

    subject = "Update on Your Request"
    body = notification_message
    email_service.send_email(user_email, subject, body)

    emit('status_update', {'request_id': request_id, 'status': status, 'user_id': user_id}, broadcast=True)