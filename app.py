# Epic Title: Real-time Status Updates and Notifications

from datetime import datetime, timedelta
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from flask_socketio import SocketIO
from requests.auth import HTTPBasicAuth
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
from backend.status.routes import register_status_routes
from backend.status.models.request_status import RequestStatus
from backend.status.services.email_service import EmailService
from backend.authentication.models import User

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://user:password@localhost/mydatabase'
app.config['JWT_SECRET_KEY'] = 'super-secret'
app.config['JWT_ACCESS_TOKEN_EXPIRES'] = timedelta(minutes=15)
app.config['JWT_REFRESH_TOKEN_EXPIRES'] = timedelta(days=30)
app.config['JWT_TOKEN_LOCATION'] = ['cookies']
app.config['JWT_COOKIE_CSRF_PROTECT'] = True
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

mfa_service = MFAService(db)
dashboard_service = DashboardService(db)
opening_request_service = OpeningRequestService(db)
service_modification_service = ServiceModificationService(db)
approval_service = ApprovalService(db)
email_service = EmailService(app.config['SMTP_SERVER'], app.config['SMTP_PORT'], app.config['SMTP_USERNAME'], app.config['SMTP_PASSWORD'])

@app.route('/')
def index():
    return render_template('index.html', current_year=datetime.now().year)

register_auth_routes(app, db, mfa_service)
register_dashboard_routes(app, dashboard_service)
register_account_opening_routes(app, opening_request_service)
register_service_modification_routes(app, service_modification_service)
register_approval_workflow_routes(app, approval_service)
register_status_routes(app, email_service)

if __name__ == '__main__':
    import logging
    logging.basicConfig(level=logging.INFO)
    socketio.run(app, debug=True)