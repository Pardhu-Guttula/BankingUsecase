# Epic Title: Role-Based Access Control

import logging
from flask import Flask
from flask_login import LoginManager
from backend.authorization.models.user_model import db, User
from backend.authorization.models.role_model import Role
from backend.authorization.controllers.role_controller import role_bp

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://user:password@localhost/dbname'
app.config['SECRET_KEY'] = 'your_secret_key'
db.init_app(app)

login_manager = LoginManager()
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    # Epic Title: Role-Based Access Control
    return User.query.get(int(user_id))

@app.before_first_request
def create_tables():
    # Epic Title: Role-Based Access Control
    db.create_all()

app.register_blueprint(role_bp, url_prefix='/roles')

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    app.run(debug=True)