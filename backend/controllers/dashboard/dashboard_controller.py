# Epic Title: Responsive Design

from flask import Blueprint, render_template
from flask_login import login_required, current_user
from backend.services.accounts.account_service import AccountService

dashboard_controller = Blueprint('dashboard_controller', __name__)

@dashboard_controller.route('/dashboard', methods=['GET'])
@login_required
def get_dashboard():
    user_id = current_user.id
    user_accounts = AccountService.get_user_accounts(user_id)
    user_service_requests = AccountService.get_service_modification_requests(user_id)
    return render_template('dashboard.html', accounts=user_accounts, service_requests=user_service_requests)


# File 6: Update Main App to Serve Static Files and Register Blueprint in backend/app.py