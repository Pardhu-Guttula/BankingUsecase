# Epic Title: Interaction History and Documentation Upload

from flask_wtf import FlaskForm
from wtforms import FileField, IntegerField
from wtforms.validators import DataRequired

class DocumentUploadForm(FlaskForm):
    request_id = IntegerField('Request ID', validators=[DataRequired()])
    document = FileField('Document', validators=[DataRequired()])


# File 4: Document Repository to Manage Uploads in repositories/interactions/document_repository.py