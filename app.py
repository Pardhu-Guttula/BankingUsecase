# Epic Title: Core Banking System Integration

from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from flask_socketio import SocketIO
from requests.auth import HTTPBasicAuth
from backend.authentication.routes.auth_routes import auth_routes
from backend.dashboard.routes.dashboard_routes import register_dashboard_routes
from backend.account.opening_requests.routes import register_account_opening_routes
from backend.account.service_modifications.routes import register_service_modification_routes
from backend.approval_workflow.routes import register_approval_workflow_routes
from backend.status.routes import register_status_routes
from backend.history.routes import register_history_routes
from backend.access.services.email_service import EmailService
from backend.status.services import StatusService
from backend.history.services import InteractionHistoryService
from backend.documents.services import DocumentService
from backend.document_upload.routes import register_document_upload_routes
from backend.applications.routes import register_application_routes
from backend.applications.services import ApplicationService
from backend.integration.routes import register_sync_routes, register_integration_routes
from backend.integration.services import CoreBankingService
from backend.integration.data_sync import DataSyncService

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://user:password@localhost/mydatabase'
app.config['JWT_SECRET_KEY'] = 'super-secret'
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['CORE_BANKING_BASE_URL'] = 'https://corebanking.example.com/api'
app.config['CORE_BANKING_USERNAME'] = 'api_user'
app.config['CORE_BANKING_PASSWORD'] = 'secure_password'
app.config['SMTP_SERVER'] = 'smtp.example.com'
app.config['SMTP_PORT'] = 587
app.config['SMTP_USERNAME'] = 'your-email@example.com'
app.config['SMTP_PASSWORD'] = 'your-email-password'

db = SQLAlchemy(app)
jwt = JWTManager(app)
socketio = SocketIO(app, cors_allowed_origins="*")

auth = HTTPBasicAuth(app.config['CORE_BANKING_USERNAME'], app.config['CORE_BANKING_PASSWORD'])

email_service = EmailService(
    app.config['SMTP_SERVER'],
    app.config['SMTP_PORT'],
    app.config['SMTP_USERNAME'],
    app.config['SMTP_PASSWORD']
)

status_service = StatusService(db, socketio, email_service)
history_service = InteractionHistoryService(db)
document_service = DocumentService(db, app.config['UPLOAD_FOLDER'])
application_service = ApplicationService(db)
core_banking_service = CoreBankingService(db, app.config['CORE_BANKING_BASE_URL'], auth)
data_sync_service = DataSyncService(db, core_banking_service)

@app.route('/')
def index():
    return render_template('index.html')

app.register_blueprint(auth_routes, url_prefix='/auth')
register_dashboard_routes(app)
register_account_opening_routes(app)
register_service_modification_routes(app)
register_approval_workflow_routes(app)
register_status_routes(app, status_service)
register_history_routes(app, history_service)
register_document_upload_routes(app, document_service)
register_application_routes(app, application_service)
register_integration_routes(app, core_banking_service)
register_sync_routes(app, data_sync_service, db)

if __name__ == '__main__':
    import logging
    logging.basicConfig(level=logging.INFO)
    socketio.run(app, debug=True)