# Epic Title: Personalized Dashboard

from flask import Blueprint, jsonify
from flask_login import login_required, current_user
from backend.services.dashboard.dashboard_service import DashboardService

dashboard_controller = Blueprint('dashboard_controller', __name__)

@dashboard_controller.route('/dashboard', methods=['GET'])
@login_required
def get_dashboard():
    user_id = current_user.id
    dashboard_data = DashboardService.get_user_dashboard(user_id)
    return jsonify(dashboard_data)

# File 5: Register Dashboard Controller Blueprint in app.py (Already Exists, Modified)