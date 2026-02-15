# Epic Title: Implement Multi-Factor Authentication

from typing import Optional
import random

class MFAService:
    @staticmethod
    def generate_token(user_id: int) -> str:
        # Epic Title: Implement Multi-Factor Authentication
        return f'{random.randint(100000, 999999):06}'

    @staticmethod
    def send_token(user_id: int, token: str) -> None:
        # Epic Title: Implement Multi-Factor Authentication
        # In real implementation, this would send the token via SMS or email
        print(f'Sending token {token} to user {user_id}')

    @staticmethod
    def verify_token(user_id: int, token: str) -> bool:
        # Epic Title: Implement Multi-Factor Authentication
        # In real implementation, this would verify the token from a database or cache
        return token == '123456'