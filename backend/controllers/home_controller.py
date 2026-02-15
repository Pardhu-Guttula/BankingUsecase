# Epic Title: Responsive Design

from flask import Blueprint, render_template

home_controller = Blueprint('home_controller', __name__)

@home_controller.route('/')
def home():
    return render_template('home.html')


# File 4: Home Template in templates/home.html