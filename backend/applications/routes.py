# Epic Title: Interaction History and Documentation Upload

from backend.applications.controllers.application_controller import application_blueprint

def register_application_routes(app):
    app.register_blueprint(application_blueprint, url_prefix='/api')