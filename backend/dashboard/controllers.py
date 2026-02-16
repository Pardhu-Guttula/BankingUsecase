# Epic Title: Personalized Dashboard

from flask import Blueprint, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from backend.dashboard.services import DashboardService

dashboard_blueprint = Blueprint('dashboard', __name__)
# Initialize DashboardService later in app.py to inject dependencies
dashboard_service = None  # Placeholder for real instance

@dashboard_blueprint.route('/dashboard', methods=['GET'])
@jwt_required()
def get_dashboard():
    current_user_id = get_jwt_identity()
    data = dashboard_service.get_dashboard_data(current_user_id)
    return jsonify(data), 200