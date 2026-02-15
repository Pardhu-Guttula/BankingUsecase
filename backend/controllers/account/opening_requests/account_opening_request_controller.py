# Epic Title: Account Opening and Service Modifications

from flask import Blueprint, jsonify, request
from flask_login import login_required, current_user
from backend.services.account.opening_requests.account_opening_request_service import AccountOpeningRequestService

account_opening_request_controller = Blueprint('account_opening_request_controller', __name__)

@account_opening_request_controller.route('/account/opening-requests', methods=['POST'])
@login_required
def create_opening_request():
    data = request.get_json()
    account_type = data.get('account_type')

    if not account_type:
        return jsonify({'message': 'Account type is required'}), 400

    request_obj = AccountOpeningRequestService.create_request(current_user.id, account_type)
    return jsonify({
        'id': request_obj.id,
        'user_id': request_obj.user_id,
        'request_date': request_obj.request_date,
        'account_type': request_obj.account_type,
        'status': request_obj.status
    }), 201

@account_opening_request_controller.route('/account/opening-requests', methods=['GET'])
@login_required
def get_opening_requests():
    requests = AccountOpeningRequestService.get_user_requests(current_user.id)
    requests_list = [{'id': r.id, 'request_date': r.request_date, 'account_type': r.account_type, 'status': r.status} for r in requests]
    return jsonify(requests_list)


# File 5: Register Account Opening Request Controller Blueprint in app.py (Already Exists, Modified)