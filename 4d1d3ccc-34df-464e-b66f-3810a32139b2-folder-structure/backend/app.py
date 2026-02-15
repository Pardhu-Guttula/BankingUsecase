# Epic Title: Core Banking System Integration

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.update(
        SECRET_KEY='yoursecretkey',
        SQLALCHEMY_DATABASE_URI='mysql+pymysql://username:password@localhost/portal_db',
        MAIL_SERVER='smtp.example.com',
        MAIL_PORT=587,
        MAIL_USE_TLS=True,
        MAIL_USERNAME='your-email@example.com',
        MAIL_PASSWORD='your-email-password',
    )

    db.init_app(app)

    login_manager = LoginManager(app)
    login_manager.login_view = "authentication_controller.login"

    with app.app_context():
        db.create_all()

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
    from dashboard.controllers.api_controller import api_controller
    from dashboard.controllers.data_sync_controller import data_sync_controller
    from dashboard.controllers.dashboard_controller import dashboard_controller

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
    app.register_blueprint(api_controller, url_prefix='/dashboard')
    app.register_blueprint(data_sync_controller, url_prefix='/dashboard')

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)


# File 2: Update to app.py Main File in repository root