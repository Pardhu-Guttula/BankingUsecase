# Epic Title: Responsive Design

from flask import Blueprint, render_template

consistent_routes = Blueprint('consistent_routes', __name__)

@consistent_routes.route('/')
def home():
    return render_template('consistent_home.html')

@consistent_routes.route('/account')
def account():
    return render_template('consistent_account.html')

@consistent_routes.route('/dashboard')
def dashboard():
    return render_template('consistent_dashboard.html')

# File 7: Register Routes Blueprint in app.py (Already Exists, Modified)