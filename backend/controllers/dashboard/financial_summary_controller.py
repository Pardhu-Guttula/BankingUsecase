# Epic Title: Personalized Dashboard

from flask import Blueprint, jsonify
from flask_login import login_required, current_user
from backend.services.dashboard.financial_summary_service import FinancialSummaryService

financial_summary_controller = Blueprint('financial_summary_controller', __name__)

@financial_summary_controller.route('/dashboard/financial-summary', methods=['GET'])
@login_required
def get_financial_summary():
    user_id = current_user.id
    financial_summary = FinancialSummaryService.get_financial_summary(user_id)
    return jsonify(financial_summary)

# File 3: Register Financial Summary Controller Blueprint in app.py (Already Exists, Modified)