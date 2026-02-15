# Epic Title: Core Banking System Integration

from flask import Blueprint, request, jsonify
from flask_login import login_required
from backend.integration.services.integration_service import IntegrationService

integration_controller = Blueprint('integration_controller', __name__)

@integration_controller.route('/fetch-core-data', methods=['GET'])
@login_required
def fetch_core_data():
    endpoint = request.args.get('endpoint')
    params = request.args.to_dict()
    if not endpoint:
        return jsonify({"message": "Endpoint is required"}), 400
    
    core_data = IntegrationService.fetch_core_banking_data(endpoint, params)
    if core_data:
        return jsonify(core_data), 200
    return jsonify({"message": "Failed to fetch data from core banking system"}), 500


# File 5: Update Main App to Register Integration Controller in app.py