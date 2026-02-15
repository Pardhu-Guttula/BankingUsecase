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

# File 5: Register Request Status Controller Blueprint in app.py (Already Exists, Modified)