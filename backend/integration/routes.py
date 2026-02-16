# Epic Title: Core Banking System Integration

from backend.integration.controllers.core_banking_controller import core_banking_blueprint

def register_integration_routes(app):
    app.register_blueprint(core_banking_blueprint, url_prefix='/api')