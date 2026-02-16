# Epic Title: Interaction History and Documentation Upload

from backend.history.controllers.history_controller import history_blueprint

def register_history_routes(app):
    app.register_blueprint(history_blueprint, url_prefix='/api')