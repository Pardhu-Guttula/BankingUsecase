# Epic Title: User Authentication and Security

from flask import Flask, send_from_directory, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from datetime import timedelta
import os
from cryptography.fernet import Fernet

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

    encryption_key = Fernet.generate_key()
    app.config['ENCRYPTION_KEY'] = encryption_key

    login_manager = LoginManager(app)
    login_manager.login_view = "auth_controller.login"
    login_manager.session_protection = "strong"

    from backend.controllers.authentication.auth_controller import auth_controller
    from backend.controllers.dashboard.dashboard_controller import dashboard_controller
    from backend.middleware.session_middleware import session_expiry_middleware

    app.register_blueprint(auth_controller, url_prefix='/auth')
    app.register_blueprint(dashboard_controller, url_prefix='/dashboard')

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


# File 5: requirements.txt Update