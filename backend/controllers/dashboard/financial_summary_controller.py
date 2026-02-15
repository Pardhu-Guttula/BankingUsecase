# Epic Title: Personalized Dashboard

from flask import Blueprint, jsonify
from flask_login import login_required, current_user
from backend.services.dashboard.financial_summary_service import FinancialSummaryService

financial_summary_controller = Blueprint('financial_summary_controller', __name__)

@financial_summary_controller.route('/dashboard/summary/accounts', methods=['GET'])
@login_required
def get_account_summary():
    account_summary = FinancialSummaryService.get_account_summary(current_user.id)
    return jsonify([{
        "id": account.id,
        "account_number": account.account_number,
        "account_type": account.account_type,
        "balance": account.balance
    } for account in account_summary]), 200

@financial_summary_controller.route('/dashboard/summary/transactions', methods=['GET'])
@login_required
def get_transaction_summary():
    transaction_summary = FinancialSummaryService.get_transaction_summary(current_user.id)
    return jsonify([{
        "id": transaction.id,
        "amount": transaction.amount,
        "type": transaction.type,
        "date": transaction.date,
        "description": transaction.description
    } for transaction in transaction_summary]), 200


# File 6: Update Main App to Register Financial Summary Controller in app.py