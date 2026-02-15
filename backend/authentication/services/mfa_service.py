# Epic Title: Implement Multi-Factor Authentication

import random
import string
from flask import current_app
from backend.authentication.models.user_model import User

class MFAService:
    @staticmethod
    def send_mfa_code(user: User) -> None:
        # Epic Title: Implement Multi-Factor Authentication
        mfa_code = ''.join(random.choices(string.digits, k=6))
        user.set_mfa_code(mfa_code)
        # Here implement logic to send `mfa_code` to the user's registered mobile device
    
    @staticmethod
    def verify_mfa_code(user: User, mfa_code: str) -> bool:
        # Epic Title: Implement Multi-Factor Authentication
        return user.check_mfa_code(mfa_code)