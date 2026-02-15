# Epic Title: Core Banking System Integration

from flask import Blueprint, jsonify, request
from flask_login import login_required
from dashboard.services.api_integration_service import APIIntegrationService

api_controller = Blueprint('api_controller', __name__)

@api_controller.route('/api/integration', methods=['POST'])
@login_required
def external_api_post():
    data = request.json
    response = APIIntegrationService.secure_post("transactions", data)
    return jsonify(response.json()), response.status_code

@api_controller.route('/api/integration', methods=['GET'])
@login_required
def external_api_get():
    response = APIIntegrationService.secure_get("transactions")
    return jsonify(response.json()), response.status_code


# File 3: App Update to Register API Controller in app.py