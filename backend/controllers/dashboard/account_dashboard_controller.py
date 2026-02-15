# Epic Title: Personalized Dashboard

from flask import Blueprint, jsonify, request
from flask_login import login_required, current_user
from backend.services.dashboard.account_dashboard_service import AccountDashboardService

account_dashboard_controller = Blueprint('account_dashboard_controller', __name__)

@account_dashboard_controller.route('/dashboard/accounts', methods=['GET'])
@login_required
def get_accounts():
    user_id = current_user.id
    account_dashboards = AccountDashboardService.get_user_account_dashboard(user_id)
    accounts_list = [{'id': acc.id, 'account_number': acc.account_number, 'account_type': acc.account_type, 'balance': acc.balance} for acc in account_dashboards]
    return jsonify(accounts_list)

# File 5: Register Dashboard Controller Blueprint in app.py (Already Exists, Modified)