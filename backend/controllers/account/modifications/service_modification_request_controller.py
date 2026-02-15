# Epic Title: Account Opening and Service Modifications

from flask import Blueprint, jsonify, request
from flask_login import login_required, current_user
from backend.services.account.modifications.service_modification_request_service import ServiceModificationRequestService

service_modification_request_controller = Blueprint('service_modification_request_controller', __name__)

@service_modification_request_controller.route('/account/modifications', methods=['POST'])
@login_required
def create_modification_request():
    data = request.get_json()
    account_id = data.get('account_id')
    service_type = data.get('service_type')

    if not account_id or not service_type:
        return jsonify({'message': 'Account ID and service type are required'}), 400

    request_obj = ServiceModificationRequestService.create_request(current_user.id, account_id, service_type)
    return jsonify({
        'id': request_obj.id,
        'user_id': request_obj.user_id,
        'account_id': request_obj.account_id,
        'request_date': request_obj.request_date,
        'service_type': request_obj.service_type,
        'status': request_obj.status
    }), 201

@service_modification_request_controller.route('/account/modifications', methods=['GET'])
@login_required
def get_modification_requests():
    requests = ServiceModificationRequestService.get_user_requests(current_user.id)
    requests_list = [{'id': r.id, 'account_id': r.account_id, 'request_date': r.request_date, 'service_type': r.service_type, 'status': r.status} for r in requests]
    return jsonify(requests_list)

# File 5: Register Service Modification Request Controller Blueprint in app.py (Already Exists, Modified)