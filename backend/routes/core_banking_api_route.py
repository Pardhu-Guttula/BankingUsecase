# Epic Title: Core Banking System Integration

from flask import Blueprint, request, jsonify
from backend.services.core_banking.core_banking_service import CoreBankingService
from backend.authentication.security.api_auth import token_required

core_banking_api_route = Blueprint('core_banking_api_route', __name__)

@core_banking_api_route.route('/api/core_banking/transaction', methods=['POST'])
@token_required
def create_transaction(user_id: int):
    data = request.get_json()
    if not data:
        return jsonify({'message': 'No data provided'}), 400
    
    transaction = CoreBankingService.create_transaction(user_id, data)
    return jsonify({
        'transaction_id': transaction.id,
        'amount': transaction.amount,
        'status': transaction.status
    })

@core_banking_api_route.route('/api/core_banking/request', methods=['POST'])
@token_required
def create_request(user_id: int):
    data = request.get_json()
    if not data:
        return jsonify({'message': 'No data provided'}), 400
    
    request = CoreBankingService.create_request(user_id, data)
    return jsonify({
        'request_id': request.id,
        'type': request.type,
        'status': request.status
    })

# File 3: Core Banking Service in services/core_banking/core_banking_service.py