from flask import Flask

def create_app():
    app = Flask(__name__)

    app.config.from_pyfile('config.py')

    from .api import models
    models.init_app(app)

    from .web import controllers
    controllers.init_app(app)

    return app