# Epic Title: Secure User Data

import bcrypt

class HashingService:
    @staticmethod
    def hash_password(password: str) -> str:
        # Epic Title: Secure User Data
        salt = bcrypt.gensalt()
        hashed = bcrypt.hashpw(password.encode(), salt)
        return hashed.decode()

    @staticmethod
    def check_password(password: str, hashed: str) -> bool:
        # Epic Title: Secure User Data
        return bcrypt.checkpw(password.encode(), hashed.encode())