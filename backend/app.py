# Epic Title: User Authentication and Security

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

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
    )

    db.init_app(app)

    login_manager = LoginManager(app)
    login_manager.login_view = "authentication_controller.login"

    from backend.controllers.authentication.authentication_controller import authentication_controller

    app.register_blueprint(authentication_controller, url_prefix='/auth')

    return app

if __name__ == '__main__':
    app = create_app()
    with app.app_context():
        db.create_all()
    app.run(debug=True)


# File 6: requirements.txt Update