# Epic Title: Develop a User-Friendly Dashboard

from backend.dashboard.controllers.dashboard_controller import dashboard_blueprint

def register_dashboard_routes(app):
    app.register_blueprint(dashboard_blueprint, url_prefix='/api')