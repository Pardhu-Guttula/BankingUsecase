# Epic Title: Account Opening and Service Modifications

from backend.approval_workflow.controllers import approval_workflow_blueprint

def register_approval_workflow_routes(app, approval_service_instance):
    global approval_service
    approval_service = approval_service_instance
    app.register_blueprint(approval_workflow_blueprint, url_prefix='/api')