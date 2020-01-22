from api.app.database.instance import db
from api.app.models.user_address import UserAddress

def map_user_address(user_address_model, user_address_schema):
    user_address_model.street = user_address_schema["street"]
    user_address_model.number = user_address_schema["number"]
    return user_address_model

def upsert_user_address(user_address_schema):
    if 'id' in user_address_schema:
        user_address = db.session.query(UserAddress).get(user_address_schema['id'])
        return map_user_address(user_address, user_address_schema)
    else:
        return map_user_address(UserAddress(), user_address_schema)


