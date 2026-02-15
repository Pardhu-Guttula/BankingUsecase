# Epic Title: Streamline Account Opening Requests

from flask import Blueprint, request, jsonify
from flask_login import login_required, current_user
from ..services.account_request_service import AccountRequestService

account_request_controller = Blueprint('account_request_controller', __name__)
account_request_service = AccountRequestService()

@account_request_controller.route('/account_requests', methods=['POST'])
@login_required
def create_account_request():
    account_type = request.json.get('account_type')

    if not account_type:
        return jsonify({"error": "Account type is required"}), 400

    success = account_request_service.create_account_request(current_user.id, account_type)
    if success:
        return jsonify({"message": "Account request submitted successfully"}), 200
    return jsonify({"error": "Failed to submit account request"}), 500

@account_request_controller.route('/account_requests', methods=['GET'])
@login_required
def get_account_requests():
    account_requests = account_request_service.get_account_requests(current_user.id)
    return jsonify(account_requests), 200



# File 4: AccountRequest Service in account/services/account_request_service.py