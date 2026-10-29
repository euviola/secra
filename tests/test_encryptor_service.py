import pytest
from secra.services.encryptor_service import Encryptor_Service

@pytest.fixture
def enc():
    return Encryptor_Service()

def test_encrypt_message_returns_encrypted_data(enc):
    msg = "message"
    assert enc.encrypt_data(msg) != msg.encode()

def test_decrypted_message_returns_original_data(enc):
    msg = "message"
    encrypted = enc.encrypt_data(msg)
    assert enc.decrypt_data(encrypted) == msg

