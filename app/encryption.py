from cryptography.fernet import Fernet
from config import Config
import base64

key = Config.SECRET_KEY[:32].encode()  # Utilisation de la clé secrète Flask
cipher_suite = Fernet(base64.urlsafe_b64encode(key))

def encrypt_data(data):
    return cipher_suite.encrypt(data.encode())

def decrypt_data(encrypted_data):
    return cipher_suite.decrypt(encrypted_data).decode()