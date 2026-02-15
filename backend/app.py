# Epic Title: In-app Notifications

from flask import Flask
from authentication.controllers.auth_controller import auth_controller
from authentication.controllers.dashboard_controller import dashboard_controller
from notifications.controllers.notification_controller import notification_controller
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from flask_login import LoginManager
from real_time import socketio, start_listener

app = Flask(__name__)
app.config.from_object('config.Config')
app.register_blueprint(auth_controller, url_prefix='/auth')
app.register_blueprint(dashboard_controller, url_prefix='/')
app.register_blueprint(notification_controller, url_prefix='/api')

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


# File 7: requirements.txt Update