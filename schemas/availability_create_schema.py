from marshmallow import Schema, fields


class CreateSchema(Schema):
    start = fields.Integer(required=True)
    end = fields.Integer(required=True)
    year = fields.Integer(required=True)
    month = fields.Integer(required=True)
    day = fields.Integer(required=True)
    av_date = fields.Date(required=True)
