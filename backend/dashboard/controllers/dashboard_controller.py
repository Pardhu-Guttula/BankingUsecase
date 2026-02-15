# Epic Title: Personalized Dashboard

from flask import Blueprint, render_template
from flask_login import login_required, current_user
from backend.dashboard.services.dashboard_service import DashboardService

dashboard_controller = Blueprint('dashboard_controller', __name__)

@dashboard_controller.route('/dashboard', methods=['GET'])
@login_required
def dashboard():
    data = DashboardService.get_dashboard_data(current_user.id)
    return render_template('dashboard.html', data=data)


# File 5: Dashboard HTML Template to Display Relevant Data in templates/dashboard.html