import marshmallow as ma


class SoftwareOrder(ma.Schema):
    id = ma.fields.Integer(required=True)
    version = ma.fields.Integer(required=True)
    amount = ma.fields.Integer()
    name = ma.fields.String(dump_only=True)
