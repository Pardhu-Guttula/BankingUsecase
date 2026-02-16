# Epic Title: Core Banking System Integration

from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required, get_jwt_identity
from backend.integration.services import CoreBankingService

integration_blueprint = Blueprint('integration', __name__)
# Initialize CoreBankingService later in app.py to inject dependencies
core_banking_service = None  # Placeholder for real instance

@integration_blueprint.route('/core_banking/request', methods=['POST'])
@jwt_required()
def core_banking_request():
    current_user_id = get_jwt_identity()
    data = request.json.get('data')
    if not data:
        return jsonify({"error": "No data provided"}), 400

    try:
        response = core_banking_service.make_request(endpoint='/some_endpoint', method='POST', data=data)
        return jsonify(response), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500