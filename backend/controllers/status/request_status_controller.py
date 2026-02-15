# Epic Title: Real-time Status Updates and Notifications

from flask import Blueprint, jsonify, request
from flask_login import login_required, current_user
from backend.services.status.request_status_service import RequestStatusService

request_status_controller = Blueprint('request_status_controller', __name__)

@request_status_controller.route('/status/request/<int:request_id>', methods=['GET'])
@login_required
def get_request_status(request_id: int):
    status_obj = RequestStatusService.get_status_by_request_id(request_id)
    if not status_obj:
        return jsonify({'message': 'Request status not found'}), 404

    return jsonify({
        'id': status_obj.id,
        'request_id': status_obj.request_id,
        'status': status_obj.status,
        'last_updated': status_obj.last_updated,
        'user_id': status_obj.user_id
    })

@request_status_controller.route('/status/user/', methods=['GET'])
@login_required
def get_user_statuses():
    statuses = RequestStatusService.get_statuses_by_user_id(current_user.id)
    statuses_list = [{
        'id': s.id,
        'request_id': s.request_id,
        'status': s.status,
        'last_updated': s.last_updated,
        'user_id': s.user_id
    } for s in statuses]

    return jsonify(statuses_list)

@request_status_controller.route('/status/request', methods=['POST'])
@login_required
def create_request_status():
    data = request.get_json()
    request_id = data.get('request_id')
    status = data.get('status')
    if not request_id or not status:
        return jsonify({'message': 'Request ID and status are required'}), 400

    status_obj = RequestStatusService.create_status(request_id, status, current_user.id, current_user.email)
    return jsonify({
        'id': status_obj.id,
        'request_id': status_obj.request_id,
        'status': status_obj.status,
        'last_updated': status_obj.last_updated,
        'user_id': status_obj.user_id
    })

@request_status_controller.route('/status/request/<int:request_id>', methods=['PUT'])
@login_required
def update_request_status(request_id: int):
    data = request.get_json()
    new_status = data.get('status')
    if not new_status:
        return jsonify({'message': 'New status is required'}), 400

    RequestStatusService.update_status(request_id, new_status, current_user.email)
    return jsonify({'message': 'Request status updated successfully'})

# File 4: Register Email Notification Blueprint in app.py (Already Exists, Modified)