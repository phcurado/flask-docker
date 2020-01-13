
from flask import jsonify


def set_user_routes(app):

    @app.route('/')
    def homepage():
        return jsonify(hello='world!')

    @app.route("/user/<name>")
    def get_user_name(name):
        return "Hello {}".format(name)