# Epic Title: Account Opening and Service Modifications

from flask import Blueprint, jsonify, request
from flask_login import login_required, current_user
from backend.services.account.opening.account_opening_service import AccountOpeningService

account_opening_controller = Blueprint('account_opening_controller', __name__)

@account_opening_controller.route('/account/opening', methods=['POST'])
@login_required
def submit_account_opening():
    data = request.get_json()
    account_type = data.get('account_type')

    if not account_type:
        return jsonify({'message': 'Account type is required'}), 400

    account_opening = AccountOpeningService.submit_account_opening(current_user.id, account_type)
    return jsonify({
        'id': account_opening.id,
        'user_id': account_opening.user_id,
        'account_type': account_opening.account_type,
        'status': account_opening.status,
        'submitted_at': account_opening.submitted_at
    }), 201

@account_opening_controller.route('/account/opening', methods=['GET'])
@login_required
def get_account_openings():
    user_account_openings = AccountOpeningService.get_user_account_openings(current_user.id)
    account_openings_list = [{'id': ao.id, 'account_type': ao.account_type, 'status': ao.status, 'submitted_at': ao.submitted_at} for ao in user_account_openings]
    return jsonify(account_openings_list)

# File 5: Register Account Opening Controller Blueprint in app.py (Already Exists, Modified)