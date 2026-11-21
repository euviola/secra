"""
Encryptor_Service is a class which whole purpose is to encrypt 
or decrypt data.
"""

import base64, os
from cryptography.fernet import Fernet, InvalidToken
from cryptography.hazmat.primitives.kdf.scrypt import Scrypt

class Encryptor_Service():

    # Generate random salt (random set of bytes)
    @staticmethod
    def generate_salt() -> bytes:
        return os.urandom(16)

    # Generate key with a salt in bytes
    # A "master" string is a profile's master password
    @staticmethod
    def derive_key(master: str, salt: bytes) -> bytes:
        kdf = Scrypt(salt=salt, length=32, n=2**15, r=8, p=1)
        return base64.urlsafe_b64decode(kdf.derive(master.encode))

    # Encrypts data with a key
    @staticmethod
    def encrypt_data(plaintext: bytes, key: bytes) -> bytes:
        return Fernet(key).encrypt(plaintext)

    # Decrypts data
    def decrypt_data(token: bytes, key: bytes) -> bytes:
        try:
            return Fernet(key).decrypt(token)
        except InvalidToken:
            raise Exception("Wrong master password or data was modified.")