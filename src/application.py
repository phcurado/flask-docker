from flask import Flask
import os

def create_app():
    app = Flask(__name__)

    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("DATABASE_URL")
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    from . import models, routes
    models.init_app(app)
    routes.init_app(app)

    return app