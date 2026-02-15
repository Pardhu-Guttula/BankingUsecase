# Epic Title: User Authentication and Security

from flask import session, redirect, url_for, request
from datetime import timedelta

class SessionMiddleware:
    @staticmethod
    def before_request():
        session.permanent = True
        session.modified = True
        
        if 'last_activity' in session:
            now = datetime.now()
            last_activity = session['last_activity']
            time_delta = now - last_activity

            if timedelta(minutes=15) < time_delta:
                session.clear()
                return redirect(url_for('authentication_controller.login'))

        session['last_activity'] = datetime.now()

    @staticmethod
    def after_request(response):
        session.modified = True
        return response

# File 2: Register Session Middleware in app.py (Already Exists, Modified)