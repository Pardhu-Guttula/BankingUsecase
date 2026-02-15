# Epic Title: Implement Adaptive Layouts

from flask import Blueprint, render_template
from flask_login import login_required, current_user

dashboard = Blueprint('dashboard', __name__)

@dashboard.route('/dashboard')
@login_required
def get_dashboard():
    return render_template('dashboard.html')


# File 5: Update app.py to Register Dashboard Route