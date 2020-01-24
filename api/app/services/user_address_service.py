from sqlalchemy.orm.exc import NoResultFound
from api.base_error import BaseError
from api.app.database.instance import db
from api.app.models.user_address import UserAddress

def map_user_address(user_address_model, user_address_schema):
    user_address_model.street = user_address_schema["street"]
    user_address_model.number = user_address_schema["number"]
    return user_address_model

def upsert_user_address(user_address_schema):
    if 'id' in user_address_schema:
        try:
            user_address = db.session.query(UserAddress).filter(UserAddress.id == user_address_schema['id']).one()
            return map_user_address(user_address, user_address_schema)
        except NoResultFound as error:
            raise BaseError(error)
    else:
        return map_user_address(UserAddress(), user_address_schema)


