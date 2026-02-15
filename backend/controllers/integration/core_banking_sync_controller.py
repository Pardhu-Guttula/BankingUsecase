# Epic Title: Data Synchronization Mechanisms

from flask import Blueprint, jsonify, request
from flask_login import login_required
from backend.services.integration.core_banking_sync_service import CoreBankingSyncService

core_banking_sync_controller = Blueprint('core_banking_sync_controller', __name__)

@core_banking_sync_controller.route('/integration/sync/<string:entity>', methods=['POST'])
@login_required
def sync_entity(entity: str):
    try:
        CoreBankingSyncService.sync_entity(entity)
        return jsonify({'message': 'Data synchronized successfully for entity ' + entity}), 200
    except Exception as e:
        return jsonify({'message': str(e)}), 500

@core_banking_sync_controller.route('/integration/sync-status/<string:entity>', methods=['GET'])
@login_required
def get_sync_status(entity: str):
    try:
        sync_status = CoreBankingSyncService.get_sync_status(entity)
        if sync_status:
            return jsonify({'entity': sync_status.entity, 'last_synced': sync_status.last_synced.isoformat()}), 200
        else:
            return jsonify({'message': 'No sync record found for entity ' + entity}), 404
    except Exception as e:
        return jsonify({'message': str(e)}), 500

@core_banking_sync_controller.route('/integration/sync-statuses', methods=['GET'])
@login_required
def get_all_sync_statuses():
    try:
        sync_statuses = CoreBankingSyncService.get_all_sync_statuses()
        return jsonify([{'entity': sync_status.entity, 'last_synced': sync_status.last_synced.isoformat()} for sync_status in sync_statuses]), 200
    except Exception as e:
        return jsonify({'message': str(e)}), 500


# File 5: Schema for Core Banking Sync Table in `database/create_core_banking_sync_table.sql`