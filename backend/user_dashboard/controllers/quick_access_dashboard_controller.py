# Epic Title: Quick Access to Features

from flask import Blueprint, render_template
from flask_login import login_required, current_user

quick_access_dashboard_bp = Blueprint('quick_access_dashboard', __name__)

@quick_access_dashboard_bp.route('/dashboard')
@login_required
def dashboard():
    # Epic Title: Quick Access to Features
    return render_template('quick_access_dashboard.html')