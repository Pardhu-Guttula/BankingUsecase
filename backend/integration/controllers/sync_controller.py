# Epic Title: Core Banking System Integration

from flask import Blueprint, request, jsonify
from backend.integration.services.sync_service import SyncService

sync_controller = Blueprint('sync_controller', __name__)

@sync_controller.route('/sync', methods=['POST'])
def sync_data():
    data = request.get_json()
    entity = data.get('entity')
    entity_data = data.get('data')
    
    if not entity or not entity_data:
        return jsonify({"message": "Invalid data."}), 400
    
    if SyncService.sync_data(entity, entity_data):
        return jsonify({"message": "Data synchronized successfully."}), 200
    return jsonify({"message": "Failed to synchronize data."}), 500

@sync_controller.route('/last-sync/<string:entity>', methods=['GET'])
def get_last_sync_time(entity: str):
    last_sync_time = SyncService.get_last_sync_time(entity)
    if last_sync_time:
        return jsonify({"entity": entity, "last_sync_time": last_sync_time.strftime("%Y-%m-%d %H:%M:%S")}), 200
    return jsonify({"message": "No sync record found."}), 404


# File 5: Update Main App to Register Sync Controller in app.py