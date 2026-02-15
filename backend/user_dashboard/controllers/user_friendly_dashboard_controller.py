# Epic Title: User-Friendly Interface

from flask import Blueprint, render_template
from flask_login import login_required, current_user

user_friendly_dashboard_bp = Blueprint('user_friendly_dashboard', __name__)

@user_friendly_dashboard_bp.route('/dashboard')
@login_required
def dashboard():
    # Epic Title: User-Friendly Interface
    return render_template('user_friendly_dashboard.html')