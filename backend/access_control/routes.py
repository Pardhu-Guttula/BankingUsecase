# Epic Title: Role-based Access Control

from backend.access_control.controllers import role_blueprint

def register_role_routes(app, role_service_instance):
    global role_service
    role_service = role_service_instance
    app.register_blueprint(role_blueprint, url_prefix='/api')