# Epic Title: Implement Adaptive Layouts

from flask import Blueprint, render_template
from flask_login import login_required

dashboard_controller = Blueprint('dashboard_controller', __name__)

@dashboard_controller.route('/dashboard')
@login_required
def dashboard():
    return render_template('dashboard.html')


# File 6: App Update to Register Dashboard Controller