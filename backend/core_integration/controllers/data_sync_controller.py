# Epic Title: Data Synchronization Mechanisms

from flask import Blueprint, jsonify
from core_integration.services.data_sync_service import DataSyncService

data_sync_controller = Blueprint('data_sync_controller', __name__)

@data_sync_controller.route('/sync/<string:endpoint>', methods=['POST'])
def sync_data(endpoint: str):
    try:
        response = DataSyncService.make_request(endpoint, method="GET")
        return jsonify(response), 200
    except Exception as e:
        return jsonify({"error": f"Data sync failed: {e}"}), 500


# File 4: Register Data Sync Controller in Helper Function in core_integration/helpers.py