# Epic Title: Interaction History and Documentation Upload

from backend.document_upload.controllers import document_upload_blueprint

def register_document_upload_routes(app, document_service_instance):
    global document_service
    document_service = document_service_instance
    app.register_blueprint(document_upload_blueprint, url_prefix='/api')