# backend/app/__init__.py
from flask import Flask
from flask_pymongo import PyMongo
from flask_cors import CORS
from .config import Config

mongo = PyMongo()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    mongo.init_app(app)
    CORS(app)
    from .controllers import tabular_controller, images_controller, text_controller
    app.register_blueprint(tabular_controller, url_prefix='/tabular')
    app.register_blueprint(images_controller, url_prefix='/images')
    app.register_blueprint(text_controller, url_prefix='/text')

    return app
