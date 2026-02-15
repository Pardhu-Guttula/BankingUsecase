# Epic Title: Core Banking System Integration

from flask import Blueprint, jsonify, request
from backend.middleware.api_security import token_required
from backend.services.integration.core_banking_data_sync_service import CoreBankingDataSyncService

core_banking_data_controller = Blueprint('core_banking_data_controller', __name__)

@core_banking_data_controller.route('/api/integration/data_sync', methods=['POST'])
@token_required
def sync_core_banking_data(current_user):
    entity = request.json.get('entity')
    if not entity:
        return jsonify({'message': 'Entity type is required'}), 400

    sync_status = CoreBankingDataSyncService.sync_data(entity)
    return jsonify({
        'entity': sync_status.entity,
        'last_synced_at': sync_status.last_synced_at,
        'status': sync_status.status,
        'is_success': sync_status.is_success
    }), 200


# File 5: Update Main App to Register Core Banking Data Controller Blueprint in app.py (Already Exists, Modified)