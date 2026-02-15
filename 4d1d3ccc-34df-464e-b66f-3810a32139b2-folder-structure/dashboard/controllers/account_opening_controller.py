# Epic Title: Streamline Account Opening Requests

from flask import Blueprint, request, jsonify
from flask_login import login_required, current_user
from dashboard.services.account_opening_service import AccountOpeningService

account_opening_controller = Blueprint('account_opening_controller', __name__)

@account_opening_controller.route('/account-opening-requests', methods=['POST'])
@login_required
def request_account_opening():
    data = request.json
    account_type = data.get('account_type')
    user_id = current_user.id

    if not account_type:
        return jsonify({"error": "Account type is required"}), 400

    request = AccountOpeningService.request_account_opening(user_id, account_type)
    return jsonify({
        "id": request.id,
        "account_type": request.account_type,
        "status": request.status,
        "created_at": request.created_at
    }), 201

@account_opening_controller.route('/account-opening-requests', methods=['GET'])
@login_required
def get_user_requests():
    user_id = current_user.id
    requests = AccountOpeningService.get_user_requests(user_id)
    return jsonify(requests), 200


# File 5: App Update to Register Account Opening Controller in app.py