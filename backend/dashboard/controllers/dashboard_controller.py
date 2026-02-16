# Epic Title: Develop a User-Friendly Dashboard

from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from backend.dashboard.services.dashboard_service import DashboardService

dashboard_blueprint = Blueprint('dashboard', __name__)
dashboard_service = DashboardService(db)

@dashboard_blueprint.route('/dashboard', methods=['GET'])
@jwt_required()
def get_dashboard():
    current_user_id = get_jwt_identity()
    accounts = dashboard_service.get_accounts_by_user_id(current_user_id)
    accounts_data = []
    for account in accounts:
        transactions = dashboard_service.get_transactions_by_account_id(account.id)
        accounts_data.append({
            "account": {
                "account_number": account.account_number,
                "account_type": account.account_type,
                "balance": account.balance,
                "created_at": account.created_at
            },
            "transactions": [
                {
                    "amount": transaction.amount,
                    "transaction_type": transaction.transaction_type,
                    "description": transaction.description,
                    "created_at": transaction.created_at
                }
                for transaction in transactions
            ]
        })
    
    return jsonify({"accounts": accounts_data}), 200