# Epic Title: Real-time Status Updates and Notifications

from flask import Blueprint, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from flask_socketio import emit
from backend.status.models.request_status import RequestStatus, db
from backend.status.services.email_service import EmailService

status_blueprint = Blueprint('status', __name__)
email_service = None  # Will be initialized in app.py

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

def emit_status_update(request_id: int, status: str, user_email: str) -> None:
    new_status = RequestStatus(request_id=request_id, status=status)
    db.session.add(new_status)
    db.session.commit()

    subject = "Update on Your Request"
    body = f"Your request with ID {request_id} has been updated to: {status}"
    email_service.send_email(user_email, subject, body)

    emit('status_update', {'request_id': request_id, 'status': status}, broadcast=True)