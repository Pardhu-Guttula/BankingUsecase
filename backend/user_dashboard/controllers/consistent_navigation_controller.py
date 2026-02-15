# Epic Title: Consistent User Experience

from flask import Blueprint, render_template
from flask_login import login_required

consistent_navigation_bp = Blueprint('consistent_navigation', __name__)

@consistent_navigation_bp.route('/dashboard')
@login_required
def dashboard():
    # Epic Title: Consistent User Experience
    return render_template('consistent_dashboard.html')