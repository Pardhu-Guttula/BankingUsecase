# Epic Title: Customizable Widgets

from backend.dashboard.controllers.widget_controller import widget_blueprint

def register_widget_routes(app):
    app.register_blueprint(widget_blueprint, url_prefix='/api')