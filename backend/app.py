# Epic Title: Account Opening and Service Modifications

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
    login_manager.login_view = "auth_controller.login"
    login_manager.session_protection = "strong"

    from backend.controllers.authentication.auth_controller import auth_controller
    from backend.controllers.dashboard.dashboard_controller import dashboard_controller
    from backend.account.controllers.service_modification_controller import service_modification_controller
    from backend.middleware.session_middleware import session_expiry_middleware

    app.register_blueprint(auth_controller, url_prefix='/auth')
    app.register_blueprint(dashboard_controller, url_prefix='/dashboard')
    app.register_blueprint(service_modification_controller, url_prefix='/account')

    session_expiry_middleware(app)

    @app.route('/')
    def home():
        return render_template('home.html')

    @app.route('/static/<path:filename>')
    def static_files(filename):
        return send_from_directory(app.config['STATIC_FOLDER'], filename)

    with app.app_context():
        db.create_all()

    return app

if __name__ == '__main__':
    app = create_app()
    with app.app_context():
        db.create_all()
    app.run(debug=True)


# File 8: requirements.txt Update