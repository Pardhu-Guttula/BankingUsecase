# Epic Title: Create Secure User Sessions

from flask import session
from datetime import timedelta

class SessionService:
    @staticmethod
    def configure_session(app):
        app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(minutes=15)
        app.config['SESSION_REFRESH_EACH_REQUEST'] = True


# File 2: Implementing Session Timeout in app.py