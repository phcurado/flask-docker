from flask import Blueprint, jsonify, request, current_app, abort, Response
from app.api.services.user import *
from app.web.views.user import UserSchema
from marshmallow import ValidationError
from app.base_error import BaseError
from ..utils.header import get_page, get_per_page

user_controller = Blueprint('user', __name__, url_prefix='/api/users')

@user_controller.route('', methods=['GET'])
def index():
    ## pagination
    page = get_page(request.headers)
    per_page = get_per_page(request.headers)
    pagination = list_paginate_users(page, per_page)
    ## data json
    pagination['data'] = UserSchema(many=True).dump(pagination['data'])

    return jsonify(pagination)

@user_controller.route('/<user_id>', methods=['GET'])
def show(user_id):
    user = get_user(user_id)
    result = UserSchema().dump(user)
    return jsonify(result)

@user_controller.route('', methods=['POST'])
def create():
    try:
        scheme = UserSchema()
        data = scheme.load(request.get_json())
        user = create_user(data)
        current_app.logger.info('User created Successfully')
        result = scheme.dump(user)
        return jsonify(result)
    except (BaseError, ValidationError) as error:
        current_app.logger.info(error.messages)
        return jsonify(error = error.messages), 400

@user_controller.route('/<user_id>', methods=['PUT'])
def edit(user_id):
    try:
        scheme = UserSchema()
        data = scheme.load(request.get_json())
        user = get_user(user_id)
        user = edit_user(user, data)
        result = scheme.dump(user)
        return jsonify(result)    
    except (BaseError, ValidationError) as error:
        current_app.logger.info(error.messages)
        return jsonify(error = error.messages), 400


@user_controller.route('/<user_id>', methods=['DELETE'])
def delete(user_id):
    return delete_user(user_id)
