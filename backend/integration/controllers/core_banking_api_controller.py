# Epic Title: Core Banking System Integration

from flask import Blueprint, request, jsonify
from flask_login import login_required
from backend.services.core_banking.core_banking_service import CoreBankingService

core_banking_api_controller = Blueprint('core_banking_api_controller', __name__)

@core_banking_api_controller.route('/api/v1/accounts/<account_id>', methods=['GET'])
@login_required
def get_account_info(account_id: str):
    try:
        account_info = CoreBankingService.get_account_info(account_id)
        return jsonify(account_info), 200
    except requests.HTTPError as e:
        return jsonify({"error": str(e)}), e.response.status_code

@core_banking_api_controller.route('/api/v1/accounts/<account_id>/transactions', methods=['POST'])
@login_required
def create_transaction(account_id: str):
    try:
        amount = request.json.get('amount')
        if amount is None:
            return jsonify({"error": "Amount is required"}), 400
        transaction = CoreBankingService.create_transaction(account_id, amount)
        return jsonify(transaction), 201
    except requests.HTTPError as e:
        return jsonify({"error": str(e)}), e.response.status_code


# File 3: Update Main App to Register Core Banking API Controller in app.py