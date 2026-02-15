# Epic Title: Develop a User-Friendly Dashboard

from flask import Blueprint, jsonify, request
from flask_login import login_required, current_user
from backend.dashboard.services.dashboard_service import DashboardService

dashboard_controller = Blueprint('dashboard_controller', __name__)

@dashboard_controller.route('/dashboard', methods=['GET'])
@login_required
def get_dashboard():
    accounts = DashboardService.get_user_accounts(current_user.id)
    transactions = DashboardService.get_user_transactions(current_user.id)
    return jsonify({
        'accounts': accounts,
        'transactions': transactions
    }), 200


# File 2: Dashboard Service in services/dashboard/dashboard_service.py