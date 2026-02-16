# Epic Title: Real-time Status Updates

from flask import Blueprint, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from flask_socketio import emit
from backend.status.models.request_status import RequestStatus, db

status_blueprint = Blueprint('status', __name__)

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

def emit_status_update(request_id: int, status: str) -> None:
    new_status = RequestStatus(request_id=request_id, status=status)
    db.session.add(new_status)
    db.session.commit()
    emit('status_update', {'request_id': request_id, 'status': status}, broadcast=True)