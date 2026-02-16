# Epic Title: Interaction History and Documentation Upload

from backend.documents.controllers.document_controller import document_blueprint, document_service

def register_document_routes(app, document_service_instance):
    global document_service
    document_service = document_service_instance
    app.register_blueprint(document_blueprint, url_prefix='/api')