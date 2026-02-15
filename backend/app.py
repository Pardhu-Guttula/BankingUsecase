# Epic Title: Personalized Dashboard

from flask import Flask, send_from_directory, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, current_user, logout_user
from flask_mail import Mail
from datetime import timedelta
import os

db = SQLAlchemy()
mail = Mail()

def create_app():
    app = Flask(__name__)
    app.config.update(
        SECRET_KEY='yoursecretkey',
        SQLALCHEMY_DATABASE_URI='mysql+pymysql://username:password@localhost/your_database_name',
        MAIL_SERVER='smtp.example.com',
        MAIL_PORT=587,
        MAIL_USE_TLS=True,
        MAIL_USERNAME='your-email@example.com',
        MAIL_PASSWORD='your-email-password',
        PERMANENT_SESSION_LIFETIME=timedelta(minutes=15),
        STATIC_FOLDER='static'
    )

    db.init_app(app)
    mail.init_app(app)

    login_manager = LoginManager(app)
    login_manager.login_view = "authentication_controller.login"
    login_manager.session_protection = "strong"

    from backend.authentication.controllers.authentication_controller import authentication_controller
    from backend.controllers.dashboard.dashboard_controller import dashboard_controller
    from backend.status.controllers.status_controller import status_controller
    from backend.history.controllers.interaction_controller import interaction_controller
    from backend.documents.controllers.document_controller import document_controller
    from backend.account.controllers.application_controller import application_controller
    from backend.integration.controllers.api_controller import api_controller
    from backend.integration.controllers.sync_controller import sync_controller
    from backend.integration.controllers.integration_controller import integration_controller
    from backend.access.controllers.role_controller import role_controller
    from backend.access_control.controllers.permission_controller import permission_controller
    from backend.access_control.controllers.policy_controller import policy_controller

    app.register_blueprint(authentication_controller, url_prefix='/auth')
    app.register_blueprint(dashboard_controller, url_prefix='/dashboard')
    app.register_blueprint(status_controller, url_prefix='/status')
    app.register_blueprint(interaction_controller, url_prefix='/history')
    app.register_blueprint(document_controller, url_prefix='/documents')
    app.register_blueprint(application_controller, url_prefix='/applications')
    app.register_blueprint(api_controller, url_prefix='/api')
    app.register_blueprint(sync_controller, url_prefix='/sync')
    app.register_blueprint(integration_controller, url_prefix='/integration')
    app.register_blueprint(role_controller, url_prefix='/roles')
    app.register_blueprint(permission_controller, url_prefix='/permissions')
    app.register_blueprint(policy_controller, url_prefix='/policies')

    @app.route('/')
    def home():
        return render_template('home.html')

    @app.route('/static/<path:filename>')
    def static_files(filename):
        return send_from_directory(app.config['STATIC_FOLDER'], filename)

    @app.before_request
    def before_request():
        session.permanent = True
        app.permanent_session_lifetime = timedelta(minutes=15)
        session.modified = True
        if current_user.is_authenticated and not current_user.is_active:
            logout_user()

    with app.app_context():
        db.create_all()

    return app

if __name__ == '__main__':
    app = create_app()
    with app.app_context():
        db.create_all()
    app.run(debug=True)


# File 8: Create Schema for Account and Transaction Tables in database/