# Epic Title: Streamline Account Opening Requests

from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from backend.account.opening_requests.services import AccountOpeningService

account_opening_blueprint = Blueprint('account_opening', __name__)
account_opening_service = AccountOpeningService(db)

@account_opening_blueprint.route('/account/opening', methods=['POST'])
@jwt_required()
def create_account_opening_request():
    current_user_id = get_jwt_identity()
    data = request.json
    account_type = data.get('account_type')
    initial_deposit = data.get('initial_deposit')
    
    if not account_type or not initial_deposit:
        return jsonify({"error": "Account type and initial deposit are required"}), 400

    opening_request = account_opening_service.create_opening_request(current_user_id, account_type, initial_deposit)
    return jsonify({
        "request_id": opening_request.id,
        "account_type": opening_request.account_type,
        "initial_deposit": opening_request.initial_deposit,
        "status": opening_request.status,
        "created_at": opening_request.created_at
    }), 201