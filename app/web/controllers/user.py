from flask import Blueprint, jsonify, request
from app.api.services.user import *
from app.web.views.user import UserSchema
import sys

user_controller = Blueprint('user', __name__, url_prefix='/api/users')

@user_controller.route('', methods=['GET'])
def index():
    user = list_users()
    schema = UserSchema(many=True)
    result = schema.dump(user)
    return jsonify(result)

@user_controller.route('/<user_id>', methods=['GET'])
def show(user_id):
    scheme = UserSchema()
    user = get_user(user_id)
    result = scheme.dump(user)
    return jsonify(result)

@user_controller.route('', methods=['POST'])
def create():
    scheme = UserSchema()
    data = scheme.load(request.get_json())
    user = create_user(data)
    result = scheme.dump(user)
    return jsonify(result)

@user_controller.route('/<user_id>', methods=['PUT'])
def edit(user_id):
    scheme = UserSchema()
    data = scheme.load(request.get_json())
    user = get_user(user_id)
    user = edit_user(user, data)
    result = scheme.dump(user)
    return jsonify(result)

@user_controller.route('/<user_id>', methods=['DELETE'])
def delete(user_id):
    return delete_user(user_id)