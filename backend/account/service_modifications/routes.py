# Epic Title: Service Modification Requests

from backend.account.service_modifications.controllers import service_modification_blueprint

def register_service_modification_routes(app):
    app.register_blueprint(service_modification_blueprint, url_prefix='/api')