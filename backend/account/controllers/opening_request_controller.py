# Epic Title: Account Opening and Service Modifications

from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required, get_jwt_identity
from backend.account.services.opening_request_service import OpeningRequestService

account_opening_blueprint = Blueprint('account_opening', __name__)
# Initialize OpeningRequestService later in app.py to inject dependencies
opening_request_service = None  # Placeholder for real instance

@account_opening_blueprint.route('/accounts/opening_requests', methods=['POST'])
@jwt_required()
def create_opening_request():
    current_user_id = get_jwt_identity()
    account_type = request.json.get('account_type')
    initial_deposit = request.json.get('initial_deposit')

    if not account_type or initial_deposit is None:
        return jsonify({"error": "Account type and initial deposit are required"}), 400

    opening_request = opening_request_service.create_opening_request(current_user_id, account_type, initial_deposit)
    return jsonify({
        "message": "Account opening request created successfully",
        "opening_request": {
            "id": opening_request.id,
            "account_type": opening_request.account_type,
            "initial_deposit": opening_request.initial_deposit,
            "status": opening_request.status,
            "created_at": opening_request.created_at
        }
    }), 201

@account_opening_blueprint.route('/accounts/opening_requests', methods=['GET'])
@jwt_required()
def get_opening_requests():
    current_user_id = get_jwt_identity()
    opening_requests = opening_request_service.get_opening_requests_for_user(current_user_id)
    return jsonify([{
        "id": req.id,
        "account_type": req.account_type,
        "initial_deposit": req.initial_deposit,
        "status": req.status,
        "created_at": req.created_at
    } for req in opening_requests]), 200