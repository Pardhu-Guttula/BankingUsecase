# Epic Title: Real-time Status Updates and Notifications

from flask import Blueprint, request, jsonify
from flask_login import login_required, current_user
from backend.services.status.request_status_service import RequestStatusService

request_status_controller = Blueprint('request_status_controller', __name__)

@request_status_controller.route('/request_status/<int:request_id>', methods=['GET'])
@login_required
def get_request_status(request_id: int):
    status = RequestStatusService.get_status(request_id=request_id, user_id=current_user.id)
    if status:
        return jsonify({
            "request_id": status.request_id,
            "status": status.status,
            "timestamp": status.timestamp,
        }), 200
    else:
        return jsonify({"message": "Status not found"}), 404


# File 6: Update Main App to Register Request Status Controller in app.py