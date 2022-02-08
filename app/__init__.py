from flask import Flask
from .config import Config
from .database import db
from routes.contacts import contacts




def create_app():
    """metodo para la creación de al app flask"""
    app = Flask(__name__, template_folder="templates")
    app.config.from_object(Config)
    db.init_app(app)
    app.register_blueprint(contacts) 
    return app


