# Epic Title: Manage Secure Storage of Credentials

from flask import Flask
from authentication.controllers.auth_controller import auth_controller
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

app = Flask(__name__)
app.register_blueprint(auth_controller, url_prefix='/auth')

DATABASE_URI = 'mysql+pymysql://username:password@localhost/db_name'
engine = create_engine(DATABASE_URI)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

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
    app.run(debug=True)



# File 8: requirements.txt Update for Secure Storage