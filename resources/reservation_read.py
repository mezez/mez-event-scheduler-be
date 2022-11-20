import configparser
from flask import jsonify

from flask_restful import Resource

from models.event_scheduler import Reservation

config = configparser.ConfigParser()
config.read('config/config.ini')


class ReservationRead(Resource):

    def get(self):

        try:
            response_payload = Reservation.query.all()
            return jsonify(response_payload)

        except:
            response = {"status_code": 500, "message": "failed"}
            return response
