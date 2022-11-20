import configparser

from flask import jsonify
from flask_restful import Resource
from models.event_scheduler import Availability

config = configparser.ConfigParser()
config.read('config/config.ini')


class AvailabilityByDate(Resource):

    def get(self, day, month, year):
        try:
            response_payload = Availability.query.filter_by(av_day=day, av_month=month, av_year=year).all()
            return jsonify(response_payload)

        except:
            response = {"status_code": 500, "message": "failed"}
            return response
