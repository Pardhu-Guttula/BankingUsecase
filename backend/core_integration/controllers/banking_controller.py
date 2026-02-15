# Epic Title: Develop Secure APIs

from flask import Blueprint, request, jsonify
from core_integration.services.banking_service import BankingService

banking_controller = Blueprint('banking_controller', __name__)

@banking_controller.route('/balance', methods=['POST'])
def get_balance():
    data = request.json
    account_id = data.get('account_id')

    if not account_id:
        return jsonify({"error": "account_id is required"}), 400

    try:
        response = BankingService.make_secure_request(f"accounts/{account_id}/balance", method="GET")
        return jsonify(response), 200
    except Exception as e:
        return jsonify({"error": f"Failed to retrieve balance: {e}"}), 500


# File 3: Register Core Banking API and Secure Blueprint in helper function in core_integration/helpers.py