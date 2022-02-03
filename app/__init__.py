from flask import Flask
from .config import Config
from .database import db




def create_app():
    """metodo para la creación de al app flask"""
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    return app