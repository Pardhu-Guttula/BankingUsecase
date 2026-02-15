# Epic Title: Real-time Status Updates

from flask import Blueprint, request, jsonify
from flask_login import login_required
from backend.services.status.request_status_service import RequestStatusService

request_status_controller = Blueprint('request_status_controller', __name__)

@request_status_controller.route('/status/requests', methods=['POST'])
@login_required
def create_status():
    data = request.get_json()
    request_id = data.get('request_id')
    status = data.get('status')
    request_type = data.get('request_type')

    if not request_id or not status or not request_type:
        return jsonify({'message': 'Request ID, status, and request type are required'}), 400

    RequestStatusService.create_status(request_id, status, request_type)
    return jsonify({'message': 'Status created successfully'}), 201

@request_status_controller.route('/status/requests', methods=['PUT'])
@login_required
def update_status():
    data = request.get_json()
    request_id = data.get('request_id')
    status = data.get('status')

    if not request_id or not status:
        return jsonify({'message': 'Request ID and status are required'}), 400

    RequestStatusService.update_status(request_id, status)
    return jsonify({'message': 'Status updated successfully'}), 200

@request_status_controller.route('/status/requests', methods=['GET'])
@login_required
def get_statuses():
    request_id = request.args.get('request_id')

    if not request_id:
        return jsonify({'message': 'Request ID is required'}), 400

    statuses = RequestStatusService.get_statuses_by_request(request_id)
    return jsonify({'statuses': [status.serialize() for status in statuses]}), 200


# File 5: Schema for Real-time Status Updates Table in `database/create_request_statuses_table.sql`