# Epic Title: Implement Multi-Factor Authentication

import random
import logging
from django.core.mail import send_mail
from django.contrib.auth.models import User

logger = logging.getLogger(__name__)

class MFAService:
    @staticmethod
    def has_second_factor(user: User) -> bool:
        # Epic Title: Implement Multi-Factor Authentication
        return hasattr(user, 'profile') and user.profile.phone_number is not None

    @staticmethod
    def send_second_factor_code(user: User) -> None:
        # Epic Title: Implement Multi-Factor Authentication
        code = random.randint(100000, 999999)
        user.profile.mfa_code = code
        user.profile.save()
        
        send_mail(
            'Your authentication code',
            f'Your code is {code}',
            'from@example.com',
            [user.email],
        )
        logger.info(f'Sent MFA code to user {user.username}')

    @staticmethod
    def check_code(user: User, code: int) -> bool:
        # Epic Title: Implement Multi-Factor Authentication
        return str(user.profile.mfa_code) == str(code)