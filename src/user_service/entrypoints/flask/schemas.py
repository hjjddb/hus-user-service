import apifairy
import marshmallow as ma
from marshmallow import fields


class UserSchema(ma.Schema):
    username = fields.String()
    password = fields.String()
    email = fields.String()
    name = fields.String()
