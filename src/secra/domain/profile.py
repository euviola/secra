from secra.services.encryptor_service import Encryptor_Service

class Profile:
    def __init__(self, enc : Encryptor_Service, name : str, password : str):
        self.enc = enc
        self.name = name
        self.password_enc = self.enc.encrypt_data(message=password)

    def log_in(self, input_pass : str) -> bool:
        return input_pass == self.enc.decrypt_data(encrypted_message=self.password_enc)