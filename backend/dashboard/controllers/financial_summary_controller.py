# Epic Title: Personalized Dashboard

from flask import Blueprint, jsonify
from flask_login import login_required, current_user
from backend.services.dashboard.financial_summary_service import FinancialSummaryService

financial_summary_controller = Blueprint('financial_summary_controller', __name__)

@financial_summary_controller.route('/dashboard/summary', methods=['GET'])
@login_required
def get_user_financial_summary():
    user_id = current_user.id
    summary = FinancialSummaryService.get_financial_summary(user_id)
    if summary:
        summary_data = {
            'total_balance': summary.total_balance,
            'total_transactions': summary.total_transactions,
        }
        return jsonify(summary_data), 200
    return jsonify({'message': 'No financial summary found'}), 404


# File 5: Register Financial Summary Controller Blueprint in app.py (Already Exists, Modified)