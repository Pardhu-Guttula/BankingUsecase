# Epic Title: Quick Access to Features

from flask import Blueprint, render_template
from flask_login import login_required

quick_access_bp = Blueprint('quick_access', __name__)

@quick_access_bp.route('/quick-access-dashboard')
@login_required
def dashboard():
    # Epic Title: Quick Access to Features
    return render_template('quick_access_dashboard.html')