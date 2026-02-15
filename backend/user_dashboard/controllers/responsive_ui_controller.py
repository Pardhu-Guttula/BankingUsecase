# Epic Title: Responsive User Interface

from flask import Blueprint, render_template
from flask_login import login_required

responsive_ui_bp = Blueprint('responsive_ui', __name__)

@responsive_ui_bp.route('/responsive-dashboard')
@login_required
def dashboard():
    # Epic Title: Responsive User Interface
    return render_template('responsive_dashboard.html')