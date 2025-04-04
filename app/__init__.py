from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

db = SQLAlchemy()
login_manager = LoginManager()

def create_app():
    """Factory qui crée et configure l'application Flask"""
    app = Flask(__name__)
    
    # Configuration (à remplacer par vos valeurs réelles)
    app.config['SECRET_KEY'] = 'votre_cle_secrete'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///patients.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    
    # Initialisation des extensions
    db.init_app(app)
    login_manager.init_app(app)
    login_manager.login_view = 'auth.login'
    
    return app