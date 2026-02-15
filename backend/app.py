# Epic Title: Overview of Financial Activities

from flask import Flask, send_from_directory, render_template, session
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, current_user, logout_user
from flask_mail import Mail
from datetime import timedelta, datetime
import os
from backend.middleware.session_middleware import SessionMiddleware

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
        STATIC_FOLDER='static',
        UPLOAD_FOLDER=os.path.join(os.getcwd(), 'backend/uploads')
    )

    if not os.path.isdir(app.config['UPLOAD_FOLDER']):
        os.makedirs(app.config['UPLOAD_FOLDER'])

    db.init_app(app)
    mail.init_app(app)

    login_manager = LoginManager(app)
    login_manager.login_view = "authentication_controller.login"
    login_manager.session_protection = "strong"

    from backend.controllers.access_control.role_controller import role_controller
    from backend.controllers.authentication.authentication_controller import authentication_controller
    from backend.controllers.portal_main_database.portal_main_controller import portal_main_controller
    from backend.controllers.dashboard.dashboard_controller import dashboard_controller

    app.register_blueprint(role_controller, url_prefix='/roles')
    app.register_blueprint(authentication_controller, url_prefix='/auth')
    app.register_blueprint(portal_main_controller, url_prefix='/portal')
    app.register_blueprint(dashboard_controller, url_prefix='/dashboard')

    app.before_request(SessionMiddleware.before_request)
    app.after_request(SessionMiddleware.after_request)

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


# File 6: Schema for Financial Activities Table in database/create_financial_activities_table.sql