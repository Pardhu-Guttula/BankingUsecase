# Epic Title: Personalized Dashboard

from backend.dashboard.controllers import dashboard_blueprint

def register_dashboard_routes(app, dashboard_service_instance):
    global dashboard_service
    dashboard_service = dashboard_service_instance
    app.register_blueprint(dashboard_blueprint, url_prefix='/api')