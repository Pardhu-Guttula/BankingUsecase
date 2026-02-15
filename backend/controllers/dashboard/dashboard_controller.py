# Epic Title: Personalized Dashboard

from flask import Blueprint, jsonify
from flask_login import login_required, current_user
from backend.services.accounts.account_service import AccountService

dashboard_controller = Blueprint('dashboard_controller', __name__)

@dashboard_controller.route('/dashboard', methods=['GET'])
@login_required
def get_dashboard():
    user_id = current_user.id
    user_accounts = AccountService.get_user_accounts(user_id)
    response = []

    for account in user_accounts:
        transactions = AccountService.get_account_transactions(account.id)
        account_info = {
            "account_number": account.account_number,
            "account_type": account.account_type,
            "balance": account.balance,
            "transactions": [{"amount": t.amount, "transaction_type": t.transaction_type, "description": t.description, "created_at": t.created_at} for t in transactions]
        }
        response.append(account_info)

    return jsonify(response), 200


# File 8: App Update to Register Dashboard Controller in app.py