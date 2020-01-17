from marshmallow import Schema, fields

class UserSchema(Schema):
    id = fields.Str()
    username = fields.Str()
    email = fields.Email()
    
user_schema = UserSchema()
users_schema = UserSchema(many=True)