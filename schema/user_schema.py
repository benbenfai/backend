from common.ma import ma
from marshmallow import validate,fields

class UserSchema(ma.Schema):
    username = fields.Str(required=True)
    password = fields.Str(required=True,
    validate=[validate.Length(min=6, max=36)])

class registerSchema(ma.Schema):
    username = fields.Str(required=True)
    email = fields.Email(required=True)
    password = fields.Str(required=True,
    validate=[validate.Length(min=6, max=36)])
