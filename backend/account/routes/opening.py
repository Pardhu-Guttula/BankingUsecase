# Epic Title: Account Opening and Service Modifications

from backend.account.controllers.opening_request_controller import account_opening_blueprint

def register_account_opening_routes(app, opening_request_service_instance):
    global opening_request_service
    opening_request_service = opening_request_service_instance
    app.register_blueprint(account_opening_blueprint, url_prefix='/api')