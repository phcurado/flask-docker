from flask import Flask, jsonify
import os

def create_app():
    app = Flask(__name__)

    from . import models

    models.init_app(app)

    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("DATABASE_URL")
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    @app.route('/')
    def homepage():
        return jsonify(hello='world!')

    @app.route("/user/<name>")
    def get_user_name(name):
        return "Hello {}".format(name)

    return app