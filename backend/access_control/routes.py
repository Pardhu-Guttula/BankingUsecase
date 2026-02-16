# Epic Title: Role-based Access Control

from backend.access_control.controllers.permission_controller import permission_blueprint

def register_access_control_routes(app):
    app.register_blueprint(permission_blueprint, url_prefix='/api')