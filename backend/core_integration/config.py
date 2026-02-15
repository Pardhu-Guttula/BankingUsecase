# Epic Title: Maintain Separate Database

import os

class Config:
    # Portal database configuration
    PORTAL_DATABASE_URI = 'mysql+pymysql://username:password@localhost/portal_db'

    # Core banking database configuration
    CORE_BANKING_DATABASE_URI = 'mysql+pymysql://username:password@localhost/core_banking_db'

    @staticmethod
    def init_app(app):
        pass


# File 2: Portal and Core Banking Database Models Initialization in core_integration/models/init.py