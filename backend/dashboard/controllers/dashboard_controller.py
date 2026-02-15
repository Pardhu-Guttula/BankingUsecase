# Epic Title: Personalized Dashboard

from flask import Blueprint, jsonify
from flask_login import login_required, current_user
from backend.services.dashboard.financial_summary_service import FinancialSummaryService

dashboard_controller = Blueprint('dashboard_controller', __name__)

@dashboard_controller.route('/dashboard', methods=['GET'])
@login_required
def get_dashboard():
    financial_summary = FinancialSummaryService.get_financial_summary(current_user.id)
    return jsonify(financial_summary), 200


# File 3: Account Repository for Fetching User Accounts in repositories/account/account_repository.py (Existing File, Re-emitting for Context)