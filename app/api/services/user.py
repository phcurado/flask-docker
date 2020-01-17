from app.api.models import User
from sqlalchemy.orm import Session
from app.api.models.base import db
from sqlalchemy.exc import SQLAlchemyError
from app.base_error import BaseError
from ..utils.paginator import Paginator
from app.web.views.user import user_schema, users_schema

def list_paginate_users(page = None, per_page = None):
    return Paginator.paginate(User, page, per_page)

def get_user(id):
    return db.session.query(User).get(id)
    
def create_user(user_schema):
    user = map(User(), user_schema)
    try:
        db.session.add(user)
        db.session.commit()
        return user
    except SQLAlchemyError as error:
        raise BaseError(error)

def edit_user(user, user_schema):
    user = map(user, user_schema)
    try:
        db.session.add(user)
        db.session.commit()
        return user
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

def query_username(username):
    return db.session.query(User).filter(User.username.like(username + '%'))

def query_email(email):
    return db.session.query(User).filter(User.email.like(email + '%'))