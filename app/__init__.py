from flask import Flask

def create_app():
    app = Flask(__name__)

    app.config.from_pyfile('config.py')

    from . import models, controllers
    models.init_app(app)
    controllers.init_app(app)

    return app