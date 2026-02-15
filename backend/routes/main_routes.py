# Epic Title: Responsive Design

from flask import Blueprint, render_template

main_routes = Blueprint('main_routes', __name__)

@main_routes.route('/')
def home():
    return render_template('home.html')

@main_routes.route('/account')
def account():
    return render_template('account.html')

@main_routes.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

# File 7: Register Routes Blueprint in app.py (Already Exists, Modified)