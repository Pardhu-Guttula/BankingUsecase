# Epic Title: Maintain Separate Database

from flask_sqlalchemy import SQLAlchemy

# Portal database
portal_db = SQLAlchemy()

# Core banking database
core_banking_db = SQLAlchemy()


# File 3: Database Initialization in app.py