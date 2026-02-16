# Epic Title: Overview of Financial Activities

from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from backend.dashboard.services.dashboard_service import DashboardService

dashboard_blueprint = Blueprint('dashboard', __name__)
dashboard_service = DashboardService(db)

@dashboard_blueprint.route('/dashboard', methods=['GET'])
@jwt_required()
def get_dashboard():
    current_user_id = get_jwt_identity()
    summary = dashboard_service.get_financial_summary(current_user_id)
    return jsonify(summary), 200