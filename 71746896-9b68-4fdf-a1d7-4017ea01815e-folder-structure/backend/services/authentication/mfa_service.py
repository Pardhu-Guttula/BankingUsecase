# Epic Title: Implement Multi-Factor Authentication

import random
from django.core.mail import send_mail
from django.contrib.auth.models import User
from typing import Any
from backend.repositories.user.user_repository import UserRepository

class MFAService:
    @staticmethod
    def send_mfa_code(user: User) -> None:
        # Epic Title: Implement Multi-Factor Authentication
        code = MFAService.generate_code()
        user_profile = UserRepository.get_profile(user)
        user_profile['mfa_code'] = code
        UserRepository.set_profile(user, user_profile)

        send_mail(
            'Your MFA Code',
            f'Your Multi-Factor Authentication code is: {code}',
            'no-reply@mywebsite.com',
            [user.email],
            fail_silently=False,
        )

    @staticmethod
    def verify_code(user_id: int, code: str) -> bool:
        # Epic Title: Implement Multi-Factor Authentication
        user = User.objects.get(id=user_id)
        user_profile = UserRepository.get_profile(user)
        return user_profile.get('mfa_code') == code

    @staticmethod
    def generate_code() -> str:
        # Epic Title: Implement Multi-Factor Authentication
        return str(random.randint(100000, 999999))