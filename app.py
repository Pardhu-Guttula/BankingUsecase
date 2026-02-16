# Epic Title: Cross-Browser Compatibility

from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from backend.authentication.routes.auth_routes import auth_routes
from backend.dashboard.routes.dashboard_routes import register_dashboard_routes
from backend.account.opening_requests.routes import register_account_opening_routes
from backend.account.service_modifications.routes import register_service_modification_routes
from backend.approval_workflow.routes import register_approval_workflow_routes

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://user:password@localhost/mydatabase'
app.config['JWT_SECRET_KEY'] = 'super-secret' 

db = SQLAlchemy(app)
jwt = JWTManager(app)

@app.route('/')
def index():
    return render_template('index.html')

app.register_blueprint(auth_routes, url_prefix='/auth')
register_dashboard_routes(app)
register_account_opening_routes(app)
register_service_modification_routes(app)
register_approval_workflow_routes(app)

if __name__ == '__main__':
    import logging
    logging.basicConfig(level=logging.INFO)
    app.run(debug=True)