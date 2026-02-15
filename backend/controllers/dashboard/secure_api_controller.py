# Epic Title: Core Banking System Integration

from flask import Blueprint, request, jsonify
from backend.services.core_banking.integration_service import IntegrationService
from flask_login import login_required

secure_api_controller = Blueprint('secure_api_controller', __name__)

@secure_api_controller.route('/api/core_banking/<string:service_name>', methods=['POST'])
@login_required
def core_banking_api(service_name: str):
    payload = request.json
    try:
        result = IntegrationService.call_core_banking_api(service_name, payload)
        return jsonify(result), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400


# File 5: Integration Management Page in templates/integration_management.html