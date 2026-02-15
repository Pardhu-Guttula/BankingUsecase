# Epic Title: Implement Secure Login Mechanism

import random
from authentication.repositories.two_factor_code_repository import TwoFactorCodeRepository
from authentication.models.two_factor_code_model import TwoFactorCode

class TwoFactorService:
    @staticmethod
    def generate_two_factor_code(user_id: int) -> str:
        code = '{:06d}'.format(random.randint(0, 999999))
        two_factor_code = TwoFactorCode(user_id, code)
        TwoFactorCodeRepository.save(two_factor_code)
        # Here you would integrate with an SMS/email service to send the code to the user
        return code

    @staticmethod
    def verify_two_factor_code(user_id: int, code: str) -> bool:
        active_code = TwoFactorCodeRepository.get_active_code(user_id)
        if active_code and active_code.code == code:
            TwoFactorCodeRepository.delete_code(active_code)
            return True
        return False


# File 6: User Authentication Service in authentication/services/authentication_service.py