# Epic Title: User-Friendly Interface

from flask import Blueprint, render_template
from flask_login import login_required

navigation_bp = Blueprint('navigation', __name__)

@navigation_bp.route('/user-friendly-dashboard')
@login_required
def dashboard():
    # Epic Title: User-Friendly Interface
    return render_template('user_friendly_dashboard.html')