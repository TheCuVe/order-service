import marshmallow as ma

class Software(ma.Schema):
    id = ma.fields.Integer(required=True)
    version = ma.fields.Integer(required=True)
    amount = ma.fields.Integer()
    name = ma.fields.String(dump_only=True)


class UpdateOrderSchema(ma.Schema):
    added = ma.fields.Nested(Software, only=('id', 'version'), many=True)
    removed = ma.fields.Nested(Software, only=('id', 'version'), many=True)
