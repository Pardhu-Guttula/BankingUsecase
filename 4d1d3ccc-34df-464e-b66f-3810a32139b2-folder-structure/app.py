# Epic Title: Develop a User-Friendly Dashboard

from flask import Flask
from authentication.controllers.authentication_controller import authentication_controller
from dashboard.controllers.dashboard_controller import dashboard_controller
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from flask_login import LoginManager
from pathlib import Path
import os

app = Flask(__name__)
app.config.update(
    SECRET_KEY='yoursecretkey',
    SQLALCHEMY_DATABASE_URI='mysql+pymysql://username:password@localhost/db_name',
)

Path("authentication/models").mkdir(parents=True, exist_ok=True)
Path("authentication/repositories").mkdir(parents=True, exist_ok=True)
Path("authentication/services").mkdir(parents=True, exist_ok=True)
Path("authentication/controllers").mkdir(parents=True, exist_ok=True)
Path("dashboard/models").mkdir(parents=True, exist_ok=True)
Path("dashboard/repositories").mkdir(parents=True, exist_ok=True)
Path("dashboard/services").mkdir(parents=True, exist_ok=True)
Path("dashboard/controllers").mkdir(parents=True, exist_ok=True)
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
app.register_blueprint(dashboard_controller, url_prefix='/dashboard')

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)


# File 8: Schema Definition for Accounts and Transactions Tables in database/10_create_accounts_and_transactions_tables.sql