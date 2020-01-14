from flask import Blueprint, jsonify, request
from app.api.services.user import *
from app.web.views.user import UserSchema
import sys

user_controller = Blueprint('user', __name__, url_prefix='/api/users')

@user_controller.route('', methods=['GET'])
def get_users():
    user = list_users()
    schema = UserSchema(many=True)
    result = schema.dump(user)
    return jsonify(result)

@user_controller.route('', methods=['POST'])
def create_user():
    data = request.get_json()
    print(data, file=sys.stderr)
    schema = UserSchema(data)
    print(data, file=sys.stderr)

    return jsonify(result='asdf')


@user_controller.route('', methods=['DELETE'])
def delete_user():
    return jsonify(hello='world!')