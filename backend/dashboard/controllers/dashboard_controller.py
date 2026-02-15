# Epic Title: Overview of Financial Activities

from flask import Blueprint, request, jsonify
from flask_login import login_required, current_user
from ..services.dashboard_service import DashboardService

dashboard_controller = Blueprint('dashboard_controller', __name__)
dashboard_service = DashboardService()

@dashboard_controller.route('/dashboard', methods=['GET'])
@login_required
def get_dashboard():
    user_id = current_user.id
    user_profile = dashboard_service.get_user_profile(user_id)
    accounts = dashboard_service.get_user_accounts(user_id)
    transactions = dashboard_service.get_user_transactions(user_id)
    financial_summary = dashboard_service.get_financial_summary(user_id)

    dashboard_data = {
        'profile': user_profile,
        'accounts': accounts,
        'transactions': transactions,
        'financial_summary': financial_summary
    }

    return jsonify(dashboard_data), 200



# File 2: Dashboard Service Update in dashboard/services/dashboard_service.py