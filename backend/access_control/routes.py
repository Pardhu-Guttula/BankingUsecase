# Epic Title: Role-based Access Control

from backend.access_control.controllers.role_controller import role_blueprint

def register_access_control_routes(app):
    app.register_blueprint(role_blueprint, url_prefix='/api')