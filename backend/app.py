# Epic Title: Secure User Data

import logging
from flask import Flask
from flask_login import LoginManager
from backend.authentication.models.user_model import db, User
from backend.authentication.controllers.user_controller import user_bp

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://user:password@localhost/dbname'
app.config['SECRET_KEY'] = 'your_secret_key'
db.init_app(app)

login_manager = LoginManager()
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    # Epic Title: Secure User Data
    return User.query.get(int(user_id))

@app.before_first_request
def create_tables():
    # Epic Title: Secure User Data
    db.create_all()

app.register_blueprint(user_bp)

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    app.run(debug=True)