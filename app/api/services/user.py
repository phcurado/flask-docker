from app.api.models import User
from sqlalchemy.orm import Session
from app.api.models.base import db

def list_users():
    return User.query.all()

def get_user(id):
    return db.session.query(User).get(id)

def create_user(user_schema):
    user = map(User(), user_schema)
    db.session.add(user)
    db.session.commit()
    return user

def edit_user(user, user_schema):
    user = map(user, user_schema)
    db.session.add(user)
    db.session.commit()
    return user

def delete_user(id):
    User.query.filter_by(id=id).delete()
    db.session.commit()
    return id

def map(user_model, user_schema):
    user_model.username = user_schema["username"]
    user_model.email = user_schema["email"]
    return user_model