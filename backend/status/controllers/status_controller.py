# Epic Title: Real-time Status Updates and Notifications

from flask import Blueprint, request, jsonify
from flask_login import login_required, current_user
from backend.status.services.status_service import StatusService

status_controller = Blueprint('status_controller', __name__)

@status_controller.route('/status', methods=['POST'])
@login_required
def create_status():
    data = request.get_json()
    request_id = data.get('request_id')
    status = data.get('status')
    if StatusService.create_status(request_id, status):
        return jsonify({"message": "Status created successfully."}), 201
    return jsonify({"message": "Failed to create status."}), 500

@status_controller.route('/status/<int:status_id>', methods=['PUT'])
@login_required
def update_status(status_id):
    data = request.get_json()
    new_status = data.get('status')
    if StatusService.update_status(status_id, new_status):
        return jsonify({"message": "Status updated successfully."}), 200
    return jsonify({"message": "Failed to update status."}), 500


# File 5: User Request Model to Manage Requests in models/status/request_model.py