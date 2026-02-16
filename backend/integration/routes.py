# Epic Title: Core Banking System Integration

from backend.integration.controllers import sync_blueprint

def register_sync_routes(app, data_sync_service_instance, db_instance):
    global data_sync_service, db
    data_sync_service = data_sync_service_instance
    db = db_instance
    app.register_blueprint(sync_blueprint, url_prefix='/api')