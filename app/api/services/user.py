from app.api.models import User

def list_users():
    return User.query.all()

def create_user(user):
    user = User.insert() \
        .values(username = user["username"])
    return user

def edit_user(user):
    user = User.update() \
        .where(id == user["id"]) \
        .values(username = user["username"])
    return user

def delete_user(id):
    return User.delete().where(id == id)