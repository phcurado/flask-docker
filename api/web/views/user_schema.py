from marshmallow import Schema, fields
from .user_address_schema import user_addresses_schema

class UserSchema(Schema):
    id = fields.Integer()
    username = fields.Str()
    email = fields.Email()
    phone = fields.Str()
    address = fields.Nested(user_addresses_schema)
    
user_schema = UserSchema()
users_schema = UserSchema(many=True)