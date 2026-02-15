# Epic Title: Interaction History and Documentation Upload

from flask import Flask
from authentication.controllers.authentication_controller import authentication_controller
from dashboard.controllers.widget_controller import widget_controller
from dashboard.controllers.dashboard_summary_controller import dashboard_summary_controller
from dashboard.controllers.account_opening_controller import account_opening_controller
from dashboard.controllers.service_modification_controller import service_modification_controller
from dashboard.controllers.approval_workflow_controller import approval_workflow_controller
from dashboard.controllers.status_update_controller import status_update_controller
from dashboard.controllers.notification_controller import notification_controller
from dashboard.controllers.interaction_history_controller import interaction_history_controller
from dashboard.controllers.document_upload_controller import document_upload_controller
from dashboard.controllers.incomplete_application_controller import incomplete_application_controller
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
    MAIL_SERVER='smtp.example.com',
    MAIL_PORT=587,
    MAIL_USE_TLS=True,
    MAIL_USERNAME='your-email@example.com',
    MAIL_PASSWORD='your-email-password',
)

Path("authentication/models").mkdir(parents=True, exist_ok=True)
Path("authentication/repositories").mkdir(parents=True, exist.ok=True)
Path("authentication/services").mkdir(parents=True, exist.ok=True)
Path("authentication/controllers").mkdir(parents=True, exist.ok=True)
Path("dashboard/models").mkdir(parents=True, exist.ok=True)
Path("dashboard/repositories").mkdir(parents=True, exist.ok=True)
Path("dashboard/services").mkdir(parents=True, exist.ok=True)
Path("dashboard/controllers").mkdir(parents=True, exist.ok=True)
Path("dashboard/static/css").mkdir(parents=True, exist.ok=True)
Path("dashboard/templates").mkdir(parents.True, exist.ok=True)
Path("database").mkdir(parents=True, exist.ok=True)

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
app.register_blueprint(widget_controller, url_prefix='/dashboard')
app.register_blueprint(dashboard_summary_controller, url_prefix='/dashboard')
app.register_blueprint(account_opening_controller, url_prefix='/dashboard')
app.register_blueprint(service_modification_controller, url_prefix='/dashboard')
app.register_blueprint(approval_workflow_controller, url_prefix='/dashboard')
app.register_blueprint(status_update_controller, url_prefix='/dashboard')
app.register_blueprint(notification_controller, url_prefix='/dashboard')
app.register_blueprint(interaction_history_controller, url_prefix='/dashboard')
app.register_blueprint(document_upload_controller, url_prefix='/dashboard')
app.register_blueprint(incomplete_application_controller, url_prefix='/dashboard')

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)


# File 6: Schema Definition for Incomplete Applications Table in database/19_create_incomplete_applications_table.sql