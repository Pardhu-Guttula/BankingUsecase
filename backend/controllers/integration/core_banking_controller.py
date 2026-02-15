# Epic Title: Develop Secure APIs

from flask import Blueprint, request, jsonify
from flask_login import login_required, current_user
from backend.services.integration.core_banking_service import CoreBankingService

core_banking_controller = Blueprint('core_banking_controller', __name__)

@core_banking_controller.route('/integration/transactions', methods=['POST'])
@login_required
def initiate_transaction():
    data = request.get_json()
    transaction_id = data.get('transaction_id')
    amount = data.get('amount')
    transaction_type = data.get('transaction_type')
    status = data.get('status')

    if not transaction_id or not amount or not transaction_type or not status:
        return jsonify({'message': 'All fields are required'}), 400

    try:
        CoreBankingService.initiate_transaction(transaction_id, amount, transaction_type, status)
        return jsonify({'message': 'Transaction initiated successfully'}), 201
    except Exception as e:
        return jsonify({'message': str(e)}), 500

@core_banking_controller.route('/integration/transactions/<string:transaction_id>', methods=['GET'])
@login_required
def get_transaction(transaction_id: str):
    try:
        transaction = CoreBankingService.get_transaction_by_id(transaction_id)
        if transaction:
            return jsonify({'transaction': transaction.serialize()}), 200
        else:
            return jsonify({'message': 'Transaction not found'}), 404
    except Exception as e:
        return jsonify({'message': str(e)}), 500

@core_banking_controller.route('/integration/transactions', methods=['GET'])
@login_required
def get_all_transactions():
    try:
        transactions = CoreBankingService.get_all_transactions()
        return jsonify({'transactions': [transaction.serialize() for transaction in transactions]}), 200
    except Exception as e:
        return jsonify({'message': str(e)}), 500


# File 5: Schema for Core Banking Transactions Table in `database/create_core_banking_transactions_table.sql`