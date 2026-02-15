# Epic Title: Core Banking System Integration

from flask import Blueprint, jsonify
from flask_login import login_required
from dashboard.services.data_sync_service import DataSyncService

data_sync_controller = Blueprint('data_sync_controller', __name__)

@data_sync_controller.route('/sync', methods=['POST'])
@login_required
def sync_data():
    try:
        DataSyncService.sync_data()
        return jsonify({"message": "Data sync successful", "last_sync": DataSyncService.get_last_sync_time()}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


# File 3: App Update to Register Data Sync Controller in app.py