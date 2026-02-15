# Epic Title: Real-time Status Updates and Notifications

from flask import Blueprint, jsonify
from flask_login import login_required, current_user
from backend.services.status.request_status_service import RequestStatusService

request_status_controller = Blueprint('request_status_controller', __name__)

@request_status_controller.route('/status/<int:request_id>', methods=['GET'])
@login_required
def get_request_status(request_id: int):
    request_status = RequestStatusService.get_request_status(request_id)
    if request_status:
        return jsonify({
            'request_id': request_status.request_id,
            'status': request_status.status,
            'updated_at': request_status.updated_at
        })
    return jsonify({'message': 'Request not found'}), 404


# File 6: Update Main App to Register Email Notification Service in app.py (Already Exists, Modified)