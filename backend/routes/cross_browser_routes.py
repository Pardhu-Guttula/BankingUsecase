# Epic Title: Responsive Design

from flask import Blueprint, render_template

cross_browser_routes = Blueprint('cross_browser_routes', __name__)

@cross_browser_routes.route('/')
def home():
    return render_template('cross_browser_home.html')

@cross_browser_routes.route('/account')
def account():
    return render_template('cross_browser_account.html')

@cross_browser_routes.route('/dashboard')
def dashboard():
    return render_template('cross_browser_dashboard.html')

# File 7: Register Routes Blueprint in app.py (Already Exists, Modified)