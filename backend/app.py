# Epic Title: Display Tailored Products

import logging
from flask import Flask
from flask_login import LoginManager
from backend.authentication.models.user_model import db, User
from backend.user_dashboard.controllers.product_dashboard_controller import product_dashboard_bp

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://user:password@localhost/dbname'
app.config['SECRET_KEY'] = 'your_secret_key'
db.init_app(app)

login_manager = LoginManager()
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    # Epic Title: Display Tailored Products
    return User.query.get(int(user_id))

@app.before_first_request
def create_tables():
    # Epic Title: Display Tailored Products
    db.create_all()

app.register_blueprint(product_dashboard_bp, url_prefix='/dashboard')

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    app.run(debug=True)