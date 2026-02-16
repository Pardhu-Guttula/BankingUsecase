# Epic Title: Streamline Account Opening Requests

from backend.account.opening_requests.controllers import account_opening_blueprint

def register_account_opening_routes(app):
    app.register_blueprint(account_opening_blueprint, url_prefix='/api')