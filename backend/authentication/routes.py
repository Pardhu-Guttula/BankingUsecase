# Epic Title: User Authentication and Security

from backend.authentication.controllers.auth_controller import auth_blueprint
from backend.authentication.controllers.mfa_controller import mfa_blueprint

def register_auth_routes(app, db_instance, mfa_service_instance):
    global db, mfa_service
    db = db_instance
    mfa_service = mfa_service_instance
    app.register_blueprint(auth_blueprint, url_prefix='/api/auth')
    app.register_blueprint(mfa_blueprint, url_prefix='/api/auth/mfa')