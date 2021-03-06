from flask import Blueprint, request, current_app, abort, jsonify
from marshmallow import ValidationError
from api.app.services.user_service import *
from api.web.views.user_schema import user_schema, users_schema
from api.base_error import BaseError
from api.web.utils.header import get_page, get_per_page

user_controller = Blueprint('user', __name__, url_prefix='/api/users')

@user_controller.route('', methods=['GET'])
def index():
    ## pages and per page options
    page = get_page(request.headers)
    per_page = get_per_page(request.headers)
    ## pagination
    pagination = list_paginate_users(request.args.to_dict(), page, per_page)
    ## data json
    pagination['data'] = users_schema.dump(pagination['data'])

    return pagination

@user_controller.route('/<user_id>', methods=['GET'])
def show(user_id):
    try:
        user = get_user(user_id)
        if user:
            return user, 201
        else:
            abort(404)
    except (BaseError, ValidationError) as error:
        current_app.logger.info(error.messages)
        return { 'error': error.messages }, 400

@user_controller.route('', methods=['POST'])
def create():
    try:
        data = user_schema.load(request.get_json())
        user = create_user(data)
        return user, 201
    except (BaseError, ValidationError) as error:
        current_app.logger.info(error.messages)
        return { 'error': error.messages }, 400

@user_controller.route('/<user_id>', methods=['PUT'])
def update(user_id):
    try:
        data = user_schema.load(request.get_json())
        user = update_user(user_id, data)
        return user, 201
    except (BaseError, ValidationError) as error:
        current_app.logger.info(error.messages)
        return { 'error': error.messages }, 400


@user_controller.route('/<user_id>', methods=['DELETE'])
def delete(user_id):
    try:
        id = delete_user(user_id)
        return id, 204
    except (BaseError, ValidationError) as error:
        current_app.logger.info(error.messages)
        return { 'error': error.messages }, 400
