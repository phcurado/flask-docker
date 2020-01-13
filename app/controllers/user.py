from flask import Blueprint, jsonify, request
import sys

# user_controller = Blueprint('user', __name__, url_prefix='/api/users')

def set_user_controller(app):
    @app.route('/api/users', methods=['GET'])
    def get_users():
        return jsonify(hello='world!')

    @app.route('/api/users', methods=['POST'])
    def create_user():
        return jsonify(hello='world!')

    @app.route("/user/<name>")
    def get_user_name(name):
        return "Hello {}".format(name)