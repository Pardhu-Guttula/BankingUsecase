# Epic Title: Consistency Across Devices

from flask import Blueprint, render_template
from flask_login import login_required, current_user

dashboard_bp = Blueprint('dashboard_bp', __name__)

@dashboard_bp.route('/dashboard', methods=['GET'])
@login_required
def dashboard():
    return render_template('dashboard.html')


# File 5: Implement Responsive Layouts with Router Integration in app.py