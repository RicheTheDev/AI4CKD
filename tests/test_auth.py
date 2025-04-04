import pytest
from app.auth import login, mfa_verify

def test_login_valid(client):
    response = client.post('/login', data={'username': 'doctor1', 'password': 'secure123'})
    assert response.status_code == 302  # Redirection vers MFA

def test_mfa_invalid(client):
    response = client.post('/mfa-verify', data={'code': '000000'})
    assert b"Invalid code" in response.data