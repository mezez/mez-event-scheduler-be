import configparser
from flask import jsonify, request

from flask_restful import Resource

from models.event_scheduler import Reservation, Availability, db

config = configparser.ConfigParser()
config.read('config/config.ini')


class ReservationDelete(Resource):

    def delete(self, id):
        # try:
        req_data = request.get_json()
        reservation = Reservation.query.filter_by(id=id, email=req_data['email'])
        reservation_data = reservation.first()
        reservation.delete()

        availability = Availability.query.get(reservation_data.availability_id)
        availability.reserved = False
        db.session.commit()

        return {"status_code": 200, "message": "success"}

    # except:
    #     response = {"status_code": 500, "message": "failed"}
    #     return response
