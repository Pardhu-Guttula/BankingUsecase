# Epic Title: Core Banking System Integration

from flask import Flask, send_from_directory, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from datetime import timedelta
import os

db = SQLAlchemy()
core_banking_db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.update(
        SECRET_KEY='yoursecretkey',
        SQLALCHEMY_DATABASE_URI='mysql+pymysql://username:password@localhost/portal_database',
        SQLALCHEMY_BINDS={
            'core_banking': 'mysql+pymysql://username:password@localhost/core_banking_database'
        },
        MAIL_SERVER='smtp.example.com',
        MAIL_PORT=587,
        MAIL_USE_TLS=True,
        MAIL_USERNAME='your-email@example.com',
        MAIL_PASSWORD='your-email-password',
        PERMANENT_SESSION_LIFETIME=timedelta(minutes=15),
        STATIC_FOLDER='static'
    )

    db.init_app(app)
    core_banking_db.init_app(app)

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

    app.register_blueprint(authentication_controller, url_prefix='/auth')
    app.register_blueprint(dashboard_controller, url_prefix='/api')
    app.register_blueprint(interaction_controller, url_prefix='/api')
    app.register_blueprint(document_controller, url_prefix='/api')
    app.register_blueprint(application_controller, url_prefix='/api')
    app.register_blueprint(secure_api_controller, url_prefix='/api')
    app.register_blueprint(sync_log_controller, url_prefix='/api')

    @app.route('/')
    def home():
        return render_template('home.html')

    @app.route('/static/<path:filename>')
    def static_files(filename):
        return send_from_directory(app.config['STATIC_FOLDER'], filename)

    from backend.services.core_banking.data_sync_scheduler import SyncScheduler
    with app.app_context():
        db.create_all()
        SyncScheduler.start(3600, "example_service")

    return app

if __name__ == '__main__':
    app = create_app()
    with app.app_context():
        db.create_all()
    app.run(debug=True)


# File 2: Core Banking Model and Repository with Separate DB Bind in models/core_banking/integration_model.py and repositories/core_banking/integration_repository.py