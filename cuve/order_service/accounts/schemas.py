import marshmallow as ma


class RegistrationSchema(ma.Schema):
    email = ma.fields.Email(required=True)
    password = ma.fields.String(required=True)

    first_name = ma.fields.String(required=True)
    last_name = ma.fields.String(required=True)
