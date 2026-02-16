# Epic Title: Core Banking System Integration

from backend.integration.controllers import integration_blueprint

def register_integration_routes(app, core_banking_service_instance):
    global core_banking_service
    core_banking_service = core_banking_service_instance
    app.register_blueprint(integration_blueprint, url_prefix='/api')