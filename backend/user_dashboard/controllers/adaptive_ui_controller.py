# Epic Title: Adaptive Screen Resolutions

from flask import Blueprint, render_template
from flask_login import login_required

adaptive_ui_bp = Blueprint('adaptive_ui', __name__)

@adaptive_ui_bp.route('/adaptive-dashboard')
@login_required
def dashboard():
    # Epic Title: Adaptive Screen Resolutions
    return render_template('adaptive_dashboard.html')