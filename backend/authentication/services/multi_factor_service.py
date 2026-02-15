# Epic Title: Implement Multi-Factor Authentication

import random
from typing import Dict

class MultiFactorService:
    otp_store: Dict[int, str] = {}

    @staticmethod
    def send_otp(user):
        # Epic Title: Implement Multi-Factor Authentication
        otp = str(random.randint(100000, 999999))
        MultiFactorService.otp_store[user.id] = otp
        # Simulate sending OTP via SMS (logging for now)
        print(f"Sending OTP {otp} to user's registered mobile {user.mobile}")

    @staticmethod
    def verify_otp(user_id: int, otp: str) -> bool:
        # Epic Title: Implement Multi-Factor Authentication
        return MultiFactorService.otp_store.get(user_id) == otp