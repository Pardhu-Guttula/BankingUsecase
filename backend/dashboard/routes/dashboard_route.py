# Epic Title: Personalized Dashboard

from flask import Blueprint, render_template
from flask_login import login_required

dashboard_route = Blueprint('dashboard_route', __name__)

@dashboard_route.route('/dashboard', methods=['GET'])
@login_required
def dashboard():
    return render_template('dashboard.html')


# File 7: HTML Template for Dashboard in templates/dashboard.html (Creating Directory and Template)