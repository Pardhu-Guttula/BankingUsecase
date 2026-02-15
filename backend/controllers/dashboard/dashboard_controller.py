# Epic Title: Overview of Financial Activities

from flask import Blueprint, jsonify, request
from flask_login import login_required, current_user
from backend.services.dashboard.financial_activity_service import FinancialActivityService

dashboard_controller = Blueprint('dashboard_controller', __name__)

@dashboard_controller.route('/dashboard', methods=['GET'])
@login_required
def get_dashboard():
    financial_summary = FinancialActivityService.get_financial_summary(current_user.id)
    return jsonify({
        'financial_summary': financial_summary
    }), 200


# File 5: Update app.py for Financial Activities Functionality