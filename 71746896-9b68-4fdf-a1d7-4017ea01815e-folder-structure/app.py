# Epic Title: Consistent User Experience

import logging
import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')

application = get_wsgi_application()

logger = logging.getLogger('myproject')

def main() -> None:
    # Epic Title: Consistent User Experience
    try:
        logger.info("Starting application...")
        # Place for additional startup code if necessary

    except Exception as e:
        logger.error(f"Error during startup: {e}")
        raise

if __name__ == "__main__":
    main()