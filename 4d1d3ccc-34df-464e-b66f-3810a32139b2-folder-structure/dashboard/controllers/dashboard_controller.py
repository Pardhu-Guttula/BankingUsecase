# Epic Title: Develop a User-Friendly Dashboard

from flask import Blueprint, jsonify
from flask_login import login_required, current_user
from dashboard.services.dashboard_service import DashboardService

dashboard_controller = Blueprint('dashboard_controller', __name__)

@dashboard_controller.route('/accounts', methods=['GET'])
@login_required
def get_user_accounts():
    user_id = current_user.id
    accounts = DashboardService.get_user_accounts(user_id)
    return jsonify(accounts), 200

@dashboard_controller.route('/accounts/<int:account_id>/transactions', methods=['GET'])
@login_required
def get_account_transactions(account_id: int):
    transactions = DashboardService.get_account_transactions(account_id)
    return jsonify(transactions), 200


# File 7: App Update to Register Dashboard Controller in app.py