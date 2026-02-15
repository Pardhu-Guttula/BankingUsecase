# Epic Title: Develop Secure APIs

from core_integration.controllers.banking_controller import banking_controller
from flask import Flask
from flask_cors import CORS

def register_blueprints(app: Flask) -> None:
    app.register_blueprint(banking_controller, url_prefix='/api/banking')


def configure_cors(app: Flask) -> None:
    CORS(app, resources={r"/api/*": {"origins": "*"}})


# File 4: Update app.py to Initialize Banking Service and Register Blueprints