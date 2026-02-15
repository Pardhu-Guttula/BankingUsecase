# Epic Title: Cross-Browser Compatibility

from flask import Blueprint, render_template
from flask_login import login_required, current_user

dashboard_bp = Blueprint('dashboard_bp', __name__)

@dashboard_bp.route('/dashboard', methods=['GET'])
@login_required
def dashboard():
    return render_template('dashboard.html')


# File 5: Update app.py to Register Dashboard Blueprint for Cross-Browser Compatibility