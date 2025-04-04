from flask import Flask
from app.routes import init_routes
from app.auth import init_auth
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

# Initialisation des modules
init_auth(app)
init_routes(app)

if __name__ == '__main__':
    app.run(ssl_context=('cert.pem', 'key.pem'))  # HTTPS obligatoire