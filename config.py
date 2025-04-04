import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or os.urandom(32)
    SQLALCHEMY_DATABASE_URI = 'sqlite:///patients.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    MFA_SECRET_LENGTH = 16  # Pour PyOTP
    SESSION_COOKIE_SECURE = True  # HTTPS only
    SESSION_COOKIE_HTTPONLY = True