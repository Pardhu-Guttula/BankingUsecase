# Epic Title: Core Banking System Integration

from flask import Blueprint, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from backend.integration.data_sync import DataSyncService

sync_blueprint = Blueprint('sync', __name__)
# Initialize DataSyncService later in app.py to inject dependencies
data_sync_service = None  # Placeholder for real instance

@sync_blueprint.route('/sync/<string:entity>', methods=['POST'])
@jwt_required()
def sync_data(entity: str):
    current_user_id = get_jwt_identity()
    try:
        data_sync_service.fetch_and_sync_data(entity)
        return jsonify({"message": f"Data synchronization for {entity} completed successfully."}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500