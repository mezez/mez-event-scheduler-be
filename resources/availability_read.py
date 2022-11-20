import configparser

from flask import jsonify
from flask_restful import Resource
from models.event_scheduler import Availability

config = configparser.ConfigParser()
config.read('config/config.ini')


class AvailabilityRead(Resource):

    def get(self):
        try:
            response_payload = Availability.query.all()
            return jsonify(response_payload)

        except:
            response = {"status_code": 500, "message": "failed"}
            return response
