# Epic Title: Service Modification Requests

from flask import Blueprint, request, jsonify
from flask_login import login_required, current_user
from backend.services.account.modifications.service_modification_request_service import ServiceModificationRequestService

service_modification_request_controller = Blueprint('service_modification_request_controller', __name__)

@service_modification_request_controller.route('/account/modifications', methods=['POST'])
@login_required
def submit_modification_request():
    data = request.get_json()
    account_id = data.get('account_id')
    modified_service = data.get('modified_service')

    if not account_id or not modified_service:
        return jsonify({'message': 'Account ID and modified service are required'}), 400

    ServiceModificationRequestService.create_request(current_user.id, account_id, modified_service)
    return jsonify({'message': 'Service modification request submitted successfully'}), 201

@service_modification_request_controller.route('/account/modifications', methods=['GET'])
@login_required
def get_modification_requests():
    requests = ServiceModificationRequestService.get_user_requests(current_user.id)
    return jsonify({'requests': [req.serialize() for req in requests]}), 200


# File 5: Schema for Service Modification Requests Table in database/create_service_modification_requests_table.sql