# Epic Title: Adaptive Screen Resolutions

from flask import Blueprint, render_template
from flask_login import login_required

adaptive_dashboard_bp = Blueprint('adaptive_dashboard', __name__)

@adaptive_dashboard_bp.route('/dashboard')
@login_required
def dashboard():
    # Epic Title: Adaptive Screen Resolutions
    return render_template('adaptive_dashboard.html')