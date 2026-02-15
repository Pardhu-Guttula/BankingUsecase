# Epic Title: Role-Based Access Control

import logging
import os
from django.core.wsgi import get_wsgi_application
from django.urls import path
from backend.controllers.authentication.role_based_access_controller import admin_dashboard_view, user_dashboard_view

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')

application = get_wsgi_application()

logger = logging.getLogger('myproject')

def main() -> None:
    # Epic Title: Role-Based Access Control
    try:
        logger.info("Starting application...")
        # Place for additional startup code if necessary

    except Exception as e:
        logger.error(f"Error during startup: {e}")
        raise

if __name__ == "__main__":
    main()

urlpatterns = [
    path('admin_dashboard/', admin_dashboard_view, name='admin_dashboard'),
    path('user_dashboard/', user_dashboard_view, name='user_dashboard'),
]