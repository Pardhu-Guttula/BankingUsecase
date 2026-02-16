# Epic Title: Role-based Access Control

from datetime import datetime, timedelta
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from flask_socketio import SocketIO
from requests.auth import HTTPBasicAuth
from backend.integration.routes import register_integration_routes
from backend.authentication.routes import register_auth_routes
from backend.authentication.services.mfa_service import MFAService
from backend.dashboard.routes import register_dashboard_routes
from backend.dashboard.services import DashboardService
from backend.account.routes.opening import register_account_opening_routes
from backend.account.services.opening_request_service import OpeningRequestService
from backend.account.routes.service_modifications import register_service_modification_routes
from backend.account.services.service_modification_service import ServiceModificationService
from backend.approval_workflow.routes import register_approval_workflow_routes
from backend.approval_workflow.services import ApprovalService
from backend.history.routes import register_history_routes
from backend.status.routes import register_status_routes
from backend.documents.routes import register_document_routes
from backend.applications.routes import register_application_routes
from backend.documents.services.document_service import DocumentService
from backend.integration.services.sync_service import SyncService
from backend.status.models.request_status import RequestStatus
from backend.status.services.email_service import EmailService
from backend.status.services.notification_service import NotificationService
from backend.history.services.interaction_service import InteractionService
from backend.applications.services.application_service import ApplicationService
from backend.authentication.models import User
from backend.access_control.routes import register_access_control_routes
from backend.middleware.auth_decorator import admin_required
from backend.access_control.models.role import db as role_db
from backend.access_control.models.permission import db as permission_db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://user:password@localhost/portal_db'
app.config['SQLALCHEMY_BINDS'] = {
    'core_banking': 'mysql://user:password@localhost/core_banking_db'
}
app.config['JWT_SECRET_KEY'] = 'super-secret'
app.config['JWT_ACCESS_TOKEN_EXPIRES'] = timedelta(minutes=15)
app.config['JWT_REFRESH_TOKEN_EXPIRES'] = timedelta(days=30)
app.config['JWT_TOKEN_LOCATION'] = ['cookies']
app.config['JWT_COOKIE_CSRF_PROTECT'] = True
app.config['UPLOAD_FOLDER'] = '/path/to/upload/folder'
app.config['CORE_BANKING_BASE_URL'] = 'https://corebanking.example.com/api'
app.config['CORE_BANKING_USERNAME'] = 'api_user'
app.config['CORE_BANKING_PASSWORD'] = 'secure_password'
app.config['SMTP_SERVER'] = 'smtp.example.com'
app.config['SMTP_PORT'] = 587
app.config['SMTP_USERNAME'] = 'your-email@example.com'
app.config['SMTP_PASSWORD'] = 'your-email-password'

role_db.init_app(app)
permission_db.init_app(app)
jwt = JWTManager(app)
socketio = SocketIO(app, cors_allowed_origins="*")

auth = HTTPBasicAuth(app.config['CORE_BANKING_USERNAME'], app.config['CORE_BANKING_PASSWORD'])

mfa_service = MFAService(role_db)
dashboard_service = DashboardService(role_db)
opening_request_service = OpeningRequestService(role_db)
service_modification_service = ServiceModificationService(role_db)
approval_service = ApprovalService(role_db)
email_service = EmailService(app.config['SMTP_SERVER'], app.config['SMTP_PORT'], app.config['SMTP_USERNAME'], app.config['SMTP_PASSWORD'])
notification_service = NotificationService(role_db)
interaction_service = InteractionService()
document_service = DocumentService(app.config['UPLOAD_FOLDER'])
application_service = ApplicationService()
sync_service = SyncService(app.config['CORE_BANKING_BASE_URL'], app.config['CORE_BANKING_USERNAME'], app.config['CORE_BANKING_PASSWORD'], role_db.create_scoped_session())

@app.route('/')
def index():
    return render_template('index.html', current_year=datetime.now().year)

@app.route('/manage-permissions')
@admin_required
def manage_permissions():
    return render_template('manage_permissions.html', current_year=datetime.now().year)

register_auth_routes(app, role_db, mfa_service)
register_dashboard_routes(app, dashboard_service)
register_account_opening_routes(app, opening_request_service)
register_service_modification_routes(app, service_modification_service)
register_approval_workflow_routes(app, approval_service)
register_history_routes(app)
register_status_routes(app, email_service, notification_service)
register_document_routes(app, document_service)
register_application_routes(app)
register_integration_routes(app, sync_service)
register_access_control_routes(app)

if __name__ == '__main__':
    import logging
    logging.basicConfig(level=logging.INFO)
    socketio.run(app, debug=True)