import pytest
from secra.domain.profile import Profile
from secra.services.encryptor_service import Encryptor_Service

@pytest.fixture
def profile():
    enc = Encryptor_Service() 
    return Profile(enc, "test-prof", "pass12345")

def test_profile_has_encrypted_password(profile):
    msg = "pass12345"
    assert profile.password_enc != msg

def test_log_in_fails_with_wrong_password(profile):
    msg = "wrongpass123450"
    assert not profile.log_in(input_pass=msg)

def test_log_in_successful_with_right_password(profile):
    msg = "pass12345"
    assert profile.log_in(input_pass=msg)