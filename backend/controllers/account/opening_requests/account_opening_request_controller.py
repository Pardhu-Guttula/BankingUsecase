# Epic Title: Streamline Account Opening Requests

from flask import Blueprint, request, jsonify
from flask_login import login_required, current_user
from backend.services.account.opening_requests.account_opening_request_service import AccountOpeningRequestService

account_opening_request_controller = Blueprint('account_opening_request_controller', __name__)

@account_opening_request_controller.route('/account/opening-requests', methods=['POST'])
@login_required
def submit_opening_request():
    data = request.get_json()
    account_type = data.get('account_type')

    if not account_type:
        return jsonify({'message': 'Account type is required'}), 400

    AccountOpeningRequestService.create_request(current_user.id, account_type)
    return jsonify({'message': 'Account opening request submitted successfully'}), 201

@account_opening_request_controller.route('/account/opening-requests', methods=['GET'])
@login_required
def get_opening_requests():
    requests = AccountOpeningRequestService.get_user_requests(current_user.id)
    return jsonify({'requests': [req.serialize() for req in requests]}), 200


# File 5: Schema for Account Opening Requests Table in database/create_account_opening_requests_table.sql