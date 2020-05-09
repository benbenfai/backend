from common.ma import ma
from marshmallow import validate,fields,ValidationError

class BytesField(fields.Field):
    def _validate(self, value):
        if not isinstance(value, bytes):
            raise ValidationError('Invalid input type.')

        if value is None or value == b'':
            raise ValidationError('Invalid value')

class Schema(ma.Schema):

    type = fields.Str(required=False)
    name = fields.Str(required=True)
    description = fields.Str(required=True)
    price = fields.Str(required=True)
    icon = BytesField(required=False)
    tdp = fields.Str(required=True)
    socket = fields.Str(required=True)
    ramtype = fields.Str(required=True)
    vram = fields.Str(required=True)
    m2 = fields.Str(required=True)
    pcapacity = fields.Str(required=True)
    bronze = fields.Str(required=True)
    rcapacity = fields.Str(required=True)
    scapacity = fields.Str(required=True)
    frequency = fields.Str(required=True)
    capacity = fields.Str(required=True)
    port = fields.Str(required=True)
    size = fields.Str(required=True)
    m2 = fields.Str(required=True)
    mbsize = fields.Str(required=True)

class cpuSchema(ma.Schema):

    cpu = fields.Str(required=False)
    description = fields.Str(required=False)
    lowprice = fields.Float(required=False)
    highprice = fields.Float(required=False)
    icon = BytesField(required=False)
    tdp = fields.Int(required=False)
    socket = fields.Str(required=False)
    ramtype = fields.Str(required=False)
    vram = fields.Int(required=False)
    m2 = fields.Str(required=False)
    pcapacity = fields.Int(required=False)
    bronze = fields.Str(required=False)
    rcapacity = fields.Int(required=False)
    capacity = fields.Int(required=False)
    port = fields.Str(required=False)

class gpuSchema(ma.Schema):

    gpu = fields.Str(required=True)
    description = fields.Str(required=True)
    lowprice = fields.Float(required=True)
    highprice = fields.Float(required=False)
    icon = BytesField(required=False)
    tdp = fields.Int(required=True)
    vram = fields.Int(required=True)

class motherboardSchema(ma.Schema):

    motherboard = fields.Str(required=True)
    description = fields.Str(required=True)
    lowprice = fields.Float(required=True)
    highprice = fields.Float(required=False)
    icon = BytesField(required=False)
    socket = fields.Str(required=True)
    ramtype = fields.Str(required=True)
    m2 = fields.Str(required=True)
    mbsize = fields.Str(required=True)

class ramSchema(ma.Schema):

    ram = fields.Str(required=True)
    description = fields.Str(required=True)
    lowprice = fields.Float(required=True)
    highprice = fields.Float(required=False)
    icon = BytesField(required=False)
    capacity = fields.Int(required=True)
    frequency = fields.Int(required=True)
    ramtype = fields.Str(required=True)

class storageSchema(ma.Schema):

    storage = fields.Str(required=True)
    description = fields.Str(required=True)
    lowprice = fields.Float(required=True)
    highprice = fields.Float(required=False)
    icon = BytesField(required=False)
    tdp = fields.Int(required=True)
    capacity = fields.Int(required=True)
    port = fields.Str(required=True)

class powersupplySchema(ma.Schema):

    powersupply = fields.Str(required=True)
    description = fields.Str(required=True)
    lowprice = fields.Float(required=True)
    highprice = fields.Float(required=False)
    icon = BytesField(required=False)
    power_capacity = fields.Int(required=True)
    bronze = fields.Str(required=True)

class casesSchema(ma.Schema):

    cases = fields.Str(required=True)
    description = fields.Str(required=True)
    lowprice = fields.Float(required=True)
    highprice = fields.Float(required=False)
    icon = BytesField(required=False)
    storagesize = fields.Str(required=True)
    mbsize = fields.Str(required=True)
