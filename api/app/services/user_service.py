from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from api.app.models.user import User
from api.app.database.instance import db
from api.base_error import BaseError
from api.web.views.user_schema import user_schema, users_schema
from ..utils.paginator import Paginator
import sys

def list_paginate_users(query_dict, page = None, per_page = None):
    query = query_builder(db.session.query(User), query_dict)
    return Paginator.paginate(query, page, per_page)

def get_user(id):    
    user = db.session.query(User).get(id)
    return user_schema.dump(user)
    
def create_user(user_params):
    user = map(User(), user_params)
    try:
        db.session.add(user)
        db.session.commit()
        return user_schema.dump(user)
    except SQLAlchemyError as error:
        raise BaseError(error)

def edit_user(id, user_params):
    user = db.session.query(User).get(id)
    user = map(user, user_params)
    try:
        db.session.add(user)
        db.session.commit()
        return user_schema.dump(user)
    except SQLAlchemyError as error:
        raise BaseError(error)


def delete_user(id):
    User.query.filter_by(id=id).delete()
    db.session.commit()
    return id

def map(user_model, user_schema):
    user_model.username = user_schema["username"]
    user_model.email = user_schema["email"]
    return user_model

def query_builder(query, query_dict):
    if 'username' in query_dict:
        query = query_by_username(query, query_dict['username'])
    if 'email' in query_dict:
        query = query_by_email(query, query_dict['email'])
    return query

def query_by_username(query, username):
    return query.filter(User.username.like(username + '%'))

def query_by_email(query, email):
    return query.filter(User.email.like(email + '%'))
