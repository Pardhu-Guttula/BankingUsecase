# Epic Title: Personalized Dashboard

from flask import Blueprint, render_template
from flask_login import login_required, current_user
from backend.dashboard.services.dashboard_service import DashboardService

dashboard_controller = Blueprint('dashboard_controller', __name__)

@dashboard_controller.route('/dashboard', methods=['GET'])
@login_required
def dashboard():
    summary = DashboardService.get_summary(current_user.id)
    return render_template('dashboard.html', summary=summary)


# File 3: Update Dashboard Template to Show Financial Summary in templates/dashboard.html