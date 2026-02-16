# Epic Title: Interaction History and Documentation Upload

from backend.applications.controllers import applications_blueprint

def register_application_routes(app, application_service_instance):
    global application_service
    application_service = application_service_instance
    app.register_blueprint(applications_blueprint, url_prefix='/api')