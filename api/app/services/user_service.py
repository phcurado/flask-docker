from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm.exc import NoResultFound
from api.app.models.user import User
from api.app.models.user_address import UserAddress
from api.app.database.instance import db
from api.base_error import BaseError
from api.web.views.user_schema import user_schema, users_schema
from ..utils.paginator import Paginator
from .user_address_service import *

def list_paginate_users(query_dict, page = None, per_page = None):
    query = query_builder(db.session.query(User), query_dict)
    return Paginator.paginate(query, page, per_page)

def get_user(id):    
    user = db.session.query(User).get(id)
    return user_schema.dump(user)
    
def create_user(user_params):
    user = map_user(User(), user_params)
    try:
        db.session.add(user)
        db.session.commit()
        return user_schema.dump(user)
    except SQLAlchemyError as error:
        db.session.rollback()
        raise BaseError(error.orig)
    finally:
        db.session.close()

def update_user(id, user_params):
    try:
        user = db.session.query(User).filter(User.id == id).one()
        user = map_user(user, user_params)
        db.session.add(user)
        db.session.commit()
        return user_schema.dump(user)
    except SQLAlchemyError as error:
        db.session.rollback()
        raise BaseError(error.orig)
    except NoResultFound as error:
        raise BaseError(error)
    finally:
        db.session.close()

def delete_user(id):
    try:
        user = db.session.query(User).get(id)
        db.session.delete(user)
        db.session.commit()
    except SQLAlchemyError as error:
        db.session.rollback()
        raise BaseError(error.orig)
    finally:
        db.session.close()
    return id

def map_user(user_model, user_schema):
    user_model.username = user_schema['username']
    user_model.email = user_schema['email']
    user_model.phone = user_schema['phone']
    if 'address' in user_schema:
        user_address = []
        for address in user_schema['address']:
            user_address.append(upsert_user_address(address))
        user_model.address = user_address
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
