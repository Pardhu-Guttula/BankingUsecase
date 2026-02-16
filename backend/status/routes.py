# Epic Title: Real-time Status Updates

from backend.status.controllers import status_blueprint

def register_status_routes(app):
    app.register_blueprint(status_blueprint, url_prefix='/api')