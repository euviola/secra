from cryptography.fernet import Fernet

class Encryptor_Service():
    def __init__(self):
        self.key = Fernet.generate_key()
        self.fernet = Fernet(self.key)

    def encrypt_data(self, message : str) -> bytes:
        return self.fernet.encrypt(message.encode())

    def decrypt_data(self, encrypted_message : bytes) -> str:
        return self.fernet.decrypt(encrypted_message).decode()