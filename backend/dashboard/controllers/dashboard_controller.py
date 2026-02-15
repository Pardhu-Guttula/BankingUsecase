# Epic Title: Personalized Dashboard

from flask import Blueprint, render_template
from flask_login import login_required, current_user
from backend.dashboard.services.dashboard_service import DashboardService

dashboard_controller = Blueprint('dashboard_controller', __name__)

@dashboard_controller.route('/dashboard', methods=['GET'])
@login_required
def dashboard():
    accounts = DashboardService.get_user_accounts(current_user.id)
    account_data = []
    for account in accounts:
        transactions = DashboardService.get_account_transactions(account.id)
        account_data.append({
            "account": account,
            "transactions": transactions
        })
    return render_template('dashboard.html', accounts=account_data)


# File 8: Dashboard Template to Display Accounts and Transactions in templates/dashboard.html