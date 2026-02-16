# Epic Title: Implement Secure Login Mechanism

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from backend.authentication.routes.auth_routes import auth_routes

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://user:password@localhost/mydatabase'

db = SQLAlchemy(app)
app.register_blueprint(auth_routes, url_prefix='/auth')

if __name__ == '__main__':
    import logging
    logging.basicConfig(level=logging.INFO)
    app.run(debug=True)