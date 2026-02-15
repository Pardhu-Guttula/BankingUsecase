# Epic Title: Maintain Separate Database

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
from core_integration.config import Config
from core_integration.models import portal_db, core_banking_db

app = Flask(__name__)
app.config.from_object(Config)
Config.init_app(app)

# Initialize databases
portal_db.init_app(app)
core_banking_db.init_app(app)

app.register_blueprint(auth_controller, url_prefix='/auth')
app.register_blueprint(application_controller, url_prefix='/api')
app.register_blueprint(document_controller, url_prefix='/api')
app.register_blueprint(interaction_controller, url_prefix='/api')

register_blueprints(app)
configure_cors(app)

portal_engine = create_engine(Config.PORTAL_DATABASE_URI)
core_banking_engine = create_engine(Config.CORE_BANKING_DATABASE_URI)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=portal_engine)

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


# File 4: Portal Database SQLAlchemy Bindings in core_integration/models/portal_db.py