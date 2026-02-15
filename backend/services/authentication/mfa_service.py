# Epic Title: Implement Secure Login Mechanism

import pyotp

class MFAService:
    @staticmethod
    def generate_secret() -> str:
        return pyotp.random_base32()

    @staticmethod
    def generate_otp(secret: str) -> str:
        totp = pyotp.TOTP(secret)
        return totp.now()

    @staticmethod
    def verify_otp(secret: str, otp: str) -> bool:
        totp = pyotp.TOTP(secret)
        return totp.verify(otp)


# File 4: Authentication Controller in controllers/authentication/authentication_controller.py