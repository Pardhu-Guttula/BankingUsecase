# Epic Title: Core Banking System Integration

from flask import Blueprint, jsonify, request
from flask_login import login_required
from backend.services.integration.core_banking_data_sync_service import CoreBankingDataSyncService

core_banking_data_sync_controller = Blueprint('core_banking_data_sync_controller', __name__)

@core_banking_data_sync_controller.route('/core-banking/sync', methods=['POST'])
@login_required
def sync_core_banking_data():
    endpoint = request.json.get('endpoint')
    if not endpoint:
        return jsonify({'message': 'Endpoint is required'}), 400
        
    CoreBankingDataSyncService.sync_data(endpoint)
    return jsonify({'message': 'Data synchronized successfully'}), 200

# File 5: Register Core Banking Data Sync Controller Blueprint in app.py (Already Exists, Modified)