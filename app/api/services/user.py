from app.api.models.user import User
from sqlalchemy.orm import Session
from app.api.database.instance import db
from sqlalchemy.exc import SQLAlchemyError
from app.base_error import BaseError
from ..utils.paginator import Paginator
from app.web.views.user import user_schema, users_schema

def list_paginate_users(page = None, per_page = None):
    return Paginator.paginate(User, page, per_page)

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

def query_username(username):
    return db.session.query(User).filter(User.username.like(username + '%'))

def query_email(email):
    return db.session.query(User).filter(User.email.like(email + '%'))