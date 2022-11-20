import configparser
from flask import jsonify, request

from flask_restful import Resource

from models.event_scheduler import Reservation, Availability, db

config = configparser.ConfigParser()
config.read('config/config.ini')


class AvailabilityDelete(Resource):

    def delete(self, id):
        try:
            Availability.query.filter_by(id=id).delete()
            db.session.commit()

            return {"status_code": 200, "message": "success"}

        except:
            response = {"status_code": 500, "message": "failed"}
            return response
