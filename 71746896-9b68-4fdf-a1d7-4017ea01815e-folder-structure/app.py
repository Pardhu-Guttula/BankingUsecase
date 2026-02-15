# Epic Title: Implement Multi-Factor Authentication

import logging
import os
from django.core.wsgi import get_wsgi_application
from django.urls import path
from backend.controllers.authentication.multi_factor_auth_controller import login_view, mfa_verify_view

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')

application = get_wsgi_application()

logger = logging.getLogger('myproject')

def main() -> None:
    # Epic Title: Implement Multi-Factor Authentication
    try:
        logger.info("Starting application...")
        # Place for additional startup code if necessary

    except Exception as e:
        logger.error(f"Error during startup: {e}")
        raise

if __name__ == "__main__":
    main()

urlpatterns = [
    path('login/', login_view, name='login'),
    path('mfa_verify/', mfa_verify_view, name='mfa_verify'),
]