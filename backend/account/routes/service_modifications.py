# Epic Title: Account Opening and Service Modifications

from backend.account.controllers.service_modification_controller import service_modification_blueprint

def register_service_modification_routes(app, service_modification_service_instance):
    global service_modification_service
    service_modification_service = service_modification_service_instance
    app.register_blueprint(service_modification_blueprint, url_prefix='/api')