# Epic Title: Overview of Financial Activities

from flask import Blueprint, jsonify
from flask_login import login_required, current_user
from dashboard.services.dashboard_summary_service import DashboardSummaryService

dashboard_summary_controller = Blueprint('dashboard_summary_controller', __name__)

@dashboard_summary_controller.route('/summary', methods=['GET'])
@login_required
def get_financial_summary():
    user_id = current_user.id
    summary = DashboardSummaryService.get_financial_summary(user_id)
    return jsonify(summary), 200


# File 3: App Update to Register Dashboard Summary Controller in app.py