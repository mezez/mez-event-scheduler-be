from marshmallow import Schema, fields


class CreateSchema(Schema):
    title = fields.String(required=True)
    email = fields.String(required=True)
    availability_id = fields.Integer(required=True)
