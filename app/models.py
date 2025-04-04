from app import db
from werkzeug.security import generate_password_hash

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password_hash = db.Column(db.String(120), nullable=False)
    mfa_secret = db.Column(db.String(32), nullable=False)  # Clé TOTP
    role = db.Column(db.String(20), nullable=False)  # 'doctor', 'admin', 'patient'

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)