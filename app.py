# Epic Title: Customizable Widgets

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from backend.authentication.routes.auth_routes import auth_routes
from backend.dashboard.routes.dashboard_routes import register_dashboard_routes
from backend.dashboard.routes.widget_routes import register_widget_routes

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://user:password@localhost/mydatabase'
app.config['JWT_SECRET_KEY'] = 'super-secret' 

db = SQLAlchemy(app)
jwt = JWTManager(app)

app.register_blueprint(auth_routes, url_prefix='/auth')
register_dashboard_routes(app)
register_widget_routes(app)

if __name__ == '__main__':
    import logging
    logging.basicConfig(level=logging.INFO)
    app.run(debug=True)