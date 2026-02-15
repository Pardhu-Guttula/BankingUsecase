# Epic Title: Personalized Dashboard

from flask import Blueprint, jsonify
from flask_login import login_required, current_user
from backend.services.dashboard.dashboard_service import DashboardService

dashboard_controller = Blueprint('dashboard_controller', __name__)

@dashboard_controller.route('/dashboard/accounts', methods=['GET'])
@login_required
def get_user_accounts():
    user_id = current_user.id
    accounts = DashboardService.get_user_accounts(user_id)
    return jsonify([{
        "id": account.id,
        "account_number": account.account_number,
        "account_type": account.account_type,
        "balance": account.balance
    } for account in accounts]), 200

@dashboard_controller.route('/dashboard/accounts/<int:account_id>/transactions', methods=['GET'])
@login_required
def get_account_transactions(account_id: int):
    transactions = DashboardService.get_account_transactions(account_id)
    return jsonify([{
        "id": transaction.id,
        "amount": transaction.amount,
        "type": transaction.type,
        "date": transaction.date,
        "description": transaction.description
    } for transaction in transactions]), 200


# File 7: Update Main App to Register Dashboard Controller in app.py