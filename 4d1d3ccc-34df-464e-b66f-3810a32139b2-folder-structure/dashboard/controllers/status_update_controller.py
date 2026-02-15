# Epic Title: Real-time Status Updates and Notifications

from flask import Blueprint, request, jsonify
from flask_login import login_required
from dashboard.services.status_update_service import StatusUpdateService

status_update_controller = Blueprint('status_update_controller', __name__)

@status_update_controller.route('/status-updates', methods=['POST'])
@login_required
def create_status_update():
    data = request.json
    request_id = data.get('request_id')
    status = data.get('status')

    if not request_id or not status:
        return jsonify({"error": "Request ID and status are required"}), 400

    status_update = StatusUpdateService.create_status_update(request_id, status)
    return jsonify({
        "id": status_update.id,
        "request_id": status_update.request_id,
        "status": status_update.status,
        "updated_at": status_update.updated_at
    }), 201

@status_update_controller.route('/status-updates/<int:request_id>', methods=['GET'])
@login_required
def get_status_updates(request_id: int):
    updates = StatusUpdateService.get_request_status_updates(request_id)
    return jsonify(updates), 200


# File 5: App Update to Register Status Update Controller in app.py