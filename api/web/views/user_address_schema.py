from marshmallow import Schema, fields

class UserAddressSchema(Schema):
    id = fields.Integer()
    street = fields.Str()
    number = fields.Integer()
    
user_address_schema = UserAddressSchema()
user_addresses_schema = UserAddressSchema(many=True)