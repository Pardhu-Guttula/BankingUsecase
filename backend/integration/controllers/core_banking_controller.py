# Epic Title: Core Banking System Integration

from flask import Blueprint, request, jsonify, current_app
from flask_jwt_extended import jwt_required, get_jwt_identity
import requests
from requests.auth import HTTPBasicAuth

core_banking_blueprint = Blueprint('core_banking', __name__)

@core_banking_blueprint.route('/api/external-data', methods=['GET'])
@jwt_required()
def get_external_data():
    user_id = get_jwt_identity()
    endpoint = current_app.config['CORE_BANKING_BASE_URL'] + '/data-endpoint'
    username = current_app.config['CORE_BANKING_USERNAME']
    password = current_app.config['CORE_BANKING_PASSWORD']

    try:
        response = requests.get(endpoint, auth=HTTPBasicAuth(username, password))

        if response.status_code == 200:
            return jsonify(response.json()), 200
        else:
            return jsonify({"error": "Failed to retrieve data", "status_code": response.status_code}), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500