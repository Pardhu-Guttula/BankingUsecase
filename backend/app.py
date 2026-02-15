# Epic Title: Access Policies for Different Roles

from flask import Flask
from authentication.controllers.auth_controller import auth_controller
from interaction_history.controllers.application_controller import application_controller
from interaction_history.controllers.document_controller import document_controller
from interaction_history.controllers.interaction_controller import interaction_controller
from core_integration.helpers import register_blueprints, configure_cors
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from flask_login import LoginManager
from real_time import socketio, start_listener
from accesscontrol.controllers.role_controller import role_controller
from accesscontrol.controllers.permission_controller import permission_controller
from accesscontrol.controllers.policy_controller import policy_controller

app = Flask(__name__)
app.config.from_object('config.Config')
app.register_blueprint(auth_controller, url_prefix='/auth')
app.register_blueprint(application_controller, url_prefix='/api')
app.register_blueprint(document_controller, url_prefix='/api')
app.register_blueprint(interaction_controller, url_prefix='/api')
app.register_blueprint(role_controller, url_prefix='/api')
app.register_blueprint(permission_controller, url_prefix='/api')
app.register_blueprint(policy_controller, url_prefix='/api')

register_blueprints(app)
configure_cors(app)

DATABASE_URI = 'mysql+pymysql://username:password@localhost/db_name'
engine = create_engine(DATABASE_URI)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

login_manager = LoginManager(app)
login_manager.login_view = "auth_controller.login"

@app.before_request
def before_request():
    # Code to handle something before a request if needed
    pass

@app.after_request
def after_request(response):
    # Code to handle something after a request if needed
    return response

@app.teardown_appcontext
def shutdown_session(exception=None):
    SessionLocal.remove()

if __name__ == '__main__':
    start_listener()
    socketio.init_app(app)
    socketio.run(app, debug=True)


# File 7: Schema Definition for Policies Table in database/07_create_policies_table.sql