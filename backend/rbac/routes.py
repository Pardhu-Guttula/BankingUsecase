# Epic Title: Role-based Access Control

from backend.rbac.controllers import rbac_blueprint

def register_rbac_routes(app, role_service_instance):
    global role_service
    role_service = role_service_instance
    app.register_blueprint(rbac_blueprint, url_prefix='/api')