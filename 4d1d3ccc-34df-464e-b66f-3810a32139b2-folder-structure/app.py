# Epic Title: Create Secure User Sessions

from flask import Flask
from authentication.controllers.authentication_controller import authentication_controller
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from flask_login import LoginManager
from authentication.services.session_service import SessionService
from pathlib import Path

app = Flask(__name__)
app.config.update(
    SECRET_KEY='yoursecretkey',
    SQLALCHEMY_DATABASE_URI='mysql+pymysql://username:password@localhost/db_name',
)

Path("authentication/models").mkdir(parents=True, exist_ok=True)
Path("authentication/repositories").mkdir(parents=True, exist_ok=True)
Path("authentication/services").mkdir(parents=True, exist_ok=True)
Path("authentication/controllers").mkdir(parents=True, exist_ok=True)
Path("database").mkdir(parents=True, exist_ok=True)

db.init_app(app)

engine = create_engine(app.config['SQLALCHEMY_DATABASE_URI'])
Session = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=engine))

login_manager = LoginManager(app)
login_manager.login_view = "authentication_controller.login"

@app.before_request
def before_request():
    # Reset the session timeout on each request
    session.modified = True

@app.teardown_appcontext
def shutdown_session(exception=None):
    Session.remove()

app.register_blueprint(authentication_controller, url_prefix='/auth')

SessionService.configure_session(app)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)


# File 3: requirements.txt Update