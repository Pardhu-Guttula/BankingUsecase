# Epic Title: Core Banking System Integration

from flask import Blueprint, jsonify
from flask_login import login_required
from backend.services.core_banking.core_banking_sync_service import CoreBankingSyncService

core_banking_sync_controller = Blueprint('core_banking_sync_controller', __name__)

@core_banking_sync_controller.route('/sync/accounts', methods=['POST'])
@login_required
def sync_accounts():
    try:
        CoreBankingSyncService.sync_accounts()
        return jsonify({"message": "Accounts synchronized successfully"}), 200
    except requests.HTTPError as e:
        return jsonify({"error": str(e)}), e.response.status_code

@core_banking_sync_controller.route('/sync/accounts/<account_id>/transactions', methods=['POST'])
@login_required
def sync_transactions(account_id: str):
    try:
        CoreBankingSyncService.sync_transactions(account_id)
        return jsonify({"message": "Transactions synchronized successfully"}), 200
    except requests.HTTPError as e:
        return jsonify({"error": str(e)}), e.response.status_code


# File 7: Update Main App to Register Core Banking Sync Controller in app.py