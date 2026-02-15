# Epic Title: Consistency Across Devices

from flask import Blueprint, render_template
from flask_login import login_required

dashboard_controller = Blueprint('dashboard_controller', __name__)

@dashboard_controller.route('/')
@login_required
def index():
    return render_template('home.html')


# File 4: App Update to Register Dashboard Home Route in app.py