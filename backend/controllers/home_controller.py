# Epic Title: Responsive Design

from flask import Blueprint, render_template

home_controller = Blueprint('home_controller', __name__)

@home_controller.route('/')
def home():
    return render_template('index.html')

# File 5: Register Home Controller Blueprint in app.py (Already Exists, Modified)