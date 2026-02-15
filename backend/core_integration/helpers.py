# Epic Title: Data Synchronization Mechanisms

from core_integration.controllers.data_sync_controller import data_sync_controller
from core_integration.controllers.banking_controller import banking_controller
from flask import Flask
from flask_cors import CORS

def register_blueprints(app: Flask) -> None:
    app.register_blueprint(data_sync_controller, url_prefix='/api/sync')
    app.register_blueprint(banking_controller, url_prefix='/api/banking')


def configure_cors(app: Flask) -> None:
    CORS(app, resources={r"/api/*": {"origins": "*"}})


# File 5: Update app.py to Register Data Sync Controller