# Epic Title: Role-based Access Control

from flask import Flask, send_from_directory, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from datetime import timedelta
import os

db = SQLAlchemy()

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

    login_manager = LoginManager(app)
    login_manager.login_view = "authentication_controller.login"
    login_manager.session_protection = "strong"

    from backend.controllers.authentication.authentication_controller import authentication_controller
    from backend.controllers.dashboard.dashboard_controller import dashboard_controller
    from backend.controllers.dashboard.interaction_controller import interaction_controller
    from backend.controllers.dashboard.document_controller import document_controller
    from backend.controllers.dashboard.application_controller import application_controller
    from backend.controllers.dashboard.secure_api_controller import secure_api_controller
    from backend.controllers.dashboard.sync_log_controller import sync_log_controller
    from backend.controllers.dashboard.role_controller import role_controller
    from backend.controllers.dashboard.permission_controller import permission_controller
    from backend.controllers.dashboard.policy_controller import policy_controller

    app.register_blueprint(authentication_controller, url_prefix='/auth')
    app.register_blueprint(dashboard_controller, url_prefix='/api')
    app.register_blueprint(interaction_controller, url_prefix='/api')
    app.register_blueprint(document_controller, url_prefix='/api')
    app.register_blueprint(application_controller, url_prefix='/api')
    app.register_blueprint(secure_api_controller, url_prefix='/api')
    app.register_blueprint(sync_log_controller, url_prefix='/api')
    app.register_blueprint(role_controller, url_prefix='/api')
    app.register_blueprint(permission_controller, url_prefix='/api')
    app.register_blueprint(policy_controller, url_prefix='/api')

    @app.route('/')
    def home():
        return render_template('home.html')

    @app.route('/static/<path:filename>')
    def static_files(filename):
        return send_from_directory(app.config['STATIC_FOLDER'], filename)

    from backend.services.core_banking.data_sync_scheduler import SyncScheduler
    with app.app_context():
        db.create_all()

    return app

if __name__ == '__main__':
    app = create_app()
    with app.app_context():
        db.create_all()
    app.run(debug=True)


# File 10: requirements.txt Update