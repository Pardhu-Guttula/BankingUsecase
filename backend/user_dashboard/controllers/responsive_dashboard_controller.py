# Epic Title: Responsive User Interface

from flask import Blueprint, render_template
from flask_login import login_required

responsive_dashboard_bp = Blueprint('responsive_dashboard', __name__)

@responsive_dashboard_bp.route('/dashboard')
@login_required
def dashboard():
    # Epic Title: Responsive User Interface
    return render_template('responsive_dashboard.html')