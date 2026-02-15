# Epic Title: Manage Secure Storage of Credentials

from flask import Flask
from authentication.controllers.authentication_controller import authentication_controller
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from flask_login import LoginManager
from pathlib import Path
from authentication.services.encryption_service import EncryptionService
import os

app = Flask(__name__)
app.config.update(
    SECRET_KEY='yoursecretkey',
    SQLALCHEMY_DATABASE_URI='mysql+pymysql://username:password@localhost/db_name',
)

# Generate and store encryption key securely
key = os.environ.get('ENCRYPTION_KEY').encode()
encryption_service = EncryptionService(key)

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

@app.teardown_appcontext
def shutdown_session(exception=None):
    Session.remove()

app.register_blueprint(authentication_controller, url_prefix='/auth')

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)


# File 7: Schema Definition for Users Table in database/09_create_users_table.sql