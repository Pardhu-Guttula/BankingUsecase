# Epic Title: Interaction History and Documentation Upload

from backend.applications.models.incomplete_application import IncompleteApplication, db

class ApplicationService:
    def __init__(self):
        pass

    def save_application_progress(self, user_id: int, form_data: str) -> IncompleteApplication:
        application = IncompleteApplication(user_id=user_id, form_data=form_data)
        db.session.add(application)
        db.session.commit()
        return application

    def get_application_progress(self, user_id: int) -> list[IncompleteApplication]:
        return IncompleteApplication.query.filter_by(user_id=user_id).all()

    def delete_application_progress(self, application_id: int) -> None:
        IncompleteApplication.query.filter_by(id=application_id).delete()
        db.session.commit()