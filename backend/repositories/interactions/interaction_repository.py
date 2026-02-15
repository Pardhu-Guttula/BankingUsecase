# Epic Title: Interaction History and Documentation Upload

from backend.models.interactions.interaction_model import Interaction

class InteractionRepository:
    @staticmethod
    def save(interaction: Interaction) -> None:
        db.session.add(interaction)
        db.session.commit()

    @staticmethod
    def find_by_user_id(user_id: int) -> list[Interaction]:
        return Interaction.query.filter_by(user_id=user_id).all()


# File 4: Interaction Service to Handle Interaction Logic in services/interactions/interaction_service.py