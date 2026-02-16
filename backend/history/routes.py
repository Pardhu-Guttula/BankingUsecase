# Epic Title: Maintain Interaction History

from backend.history.controllers import history_blueprint

def register_history_routes(app, history_service_instance):
    global history_service
    history_service = history_service_instance
    app.register_blueprint(history_blueprint, url_prefix='/api')