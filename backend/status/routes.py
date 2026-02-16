# Epic Title: Real-time Status Updates and Notifications

from backend.status.controllers.status_controller import status_blueprint, email_service

def register_status_routes(app, email_service_instance):
    global email_service
    email_service = email_service_instance
    app.register_blueprint(status_blueprint, url_prefix='/api')