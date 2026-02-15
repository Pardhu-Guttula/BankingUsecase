# Epic Title: Consistent User Experience

from flask import Blueprint, render_template
from flask_login import login_required

consistent_ui_bp = Blueprint('consistent_ui', __name__)

@consistent_ui_bp.route('/consistent-dashboard')
@login_required
def dashboard():
    # Epic Title: Consistent User Experience
    return render_template('consistent_dashboard.html')