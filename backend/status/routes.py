# Epic Title: Real-time Status Updates and Notifications

from backend.status.controllers import status_blueprint

def register_status_routes(app, status_service_instance):
    global status_service
    status_service = status_service_instance
    app.register_blueprint(status_blueprint, url_prefix='/api')