# Epic Title: Approval and Processing Workflows

from backend.approval_workflow.controllers import approval_workflow_blueprint

def register_approval_workflow_routes(app):
    app.register_blueprint(approval_workflow_blueprint, url_prefix='/api')