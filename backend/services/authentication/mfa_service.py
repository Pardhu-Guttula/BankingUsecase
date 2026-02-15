# Epic Title: User Authentication and Security

import pyotp
from backend.repositories.authentication.mfa_repository import MFARepository
from backend.models.authentication.mfa_model import MFA


class MFAService:
    @staticmethod
    def generate_secret() -> str:
        return pyotp.random_base32()

    @staticmethod
    def create_mfa(user_id: int) -> MFA:
        secret = MFAService.generate_secret()
        mfa = MFA(user_id=user_id, secret=secret)
        MFARepository.save(mfa)
        return mfa

    @staticmethod
    def verify_token(user_id: int, token: str) -> bool:
        mfa = MFARepository.get_mfa_by_user_id(user_id)
        if not mfa:
            return False

        totp = pyotp.TOTP(mfa.secret)
        return totp.verify(token)

    @staticmethod
    def confirm_mfa(user_id: int) -> None:
        mfa = MFARepository.get_mfa_by_user_id(user_id)
        if mfa:
            mfa.confirmed = True
            MFARepository.update(mfa)


# File 4: Update Authentication Controller to Include MFA in authentication/controllers/authentication_controller.py