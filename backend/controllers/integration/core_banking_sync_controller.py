# Epic Title: Core Banking System Integration

from flask import Blueprint, request, jsonify
from backend.services.integration.core_banking_sync_service import CoreBankingSyncService
from backend.authentication.security.api_auth import token_required

core_banking_sync_controller = Blueprint('core_banking_sync_controller', __name__)

@core_banking_sync_controller.route('/sync/transactions', methods=['POST'])
@token_required
def sync_transactions(user_id: int):
    data = request.json
    if not data:
        return jsonify({'message': 'No data provided'}), 400
    
    CoreBankingSyncService.sync_transactions(data)
    return jsonify({'message': 'Transactions synced successfully'})

@core_banking_sync_controller.route('/sync/requests', methods=['POST'])
@token_required
def sync_requests(user_id: int):
    data = request.json
    if not data:
        return jsonify({'message': 'No data provided'}), 400
    
    CoreBankingSyncService.sync_requests(data)
    return jsonify({'message': 'Requests synced successfully'})

# File 3: Update Transaction Model to Include External ID in models/core_banking/transaction_model.py (Modified)