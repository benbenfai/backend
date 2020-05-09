from common.ma import ma
from marshmallow import validate,fields

class listnoSchema(ma.Schema):

    listno = fields.Int(required=True)

class buildlistSchema(ma.Schema):

    listno = fields.Int(required=False)
    createDate = fields.Date(required=True,format='%d-%m-%Y')
    cost = fields.Int(required=True)
    creator = fields.Str(required=True)

class listhardwareSchema(ma.Schema):

    listno = fields.Int(required=False)
    hardware = fields.Str(required=True)
    htype = fields.Str(required=True)
