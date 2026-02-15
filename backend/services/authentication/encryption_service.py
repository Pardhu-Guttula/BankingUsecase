# Epic Title: Manage Secure Storage of Credentials

from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
import os
import base64

class EncryptionService:
    def __init__(self, key: bytes):
        self.key = key
        self.backend = default_backend()

    def encrypt(self, plaintext: str) -> str:
        iv = os.urandom(16)
        cipher = Cipher(algorithms.AES(self.key), modes.CBC(iv), backend=self.backend)
        encryptor = cipher.encryptor()
        padded_data = self._pad(plaintext.encode())
        encrypted = encryptor.update(padded_data) + encryptor.finalize()
        return base64.b64encode(iv + encrypted).decode('utf-8')

    def decrypt(self, ciphertext: str) -> str:
        data = base64.b64decode(ciphertext)
        iv = data[:16]
        cipher = Cipher(algorithms.AES(self.key), modes.CBC(iv), backend=self.backend)
        decryptor = cipher.decryptor()
        padded_data = decryptor.update(data[16:]) + decryptor.finalize()
        return self._unpad(padded_data).decode('utf-8')

    def _pad(self, data: bytes) -> bytes:
        pad_length = 16 - len(data) % 16
        return data + pad_length * chr(pad_length).encode()

    def _unpad(self, data: bytes) -> bytes:
        pad_length = data[-1]
        return data[:-pad_length]


# File 3: User Repository with Encryption and Decryption in repositories/authentication/user_repository.py