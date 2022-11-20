import json
import configparser
import requests
from flask_restful import Resource
from flask import request, jsonify
from helpers import my_helper
from schemas.reservation_create_schema import CreateSchema
from models.event_scheduler import Availability, Reservation, db


class ReservationCreate(Resource):
    # @jwt_required()
    # @auth.login_required
    def post(self):
        # try:
        # validation
        create_schema = CreateSchema()
        errors = create_schema.validate(request.json)
        if errors:
            return errors, 422

        req_data = request.get_json()

        # save data
        my_helper.saveLog("create-req:::" + json.dumps(req_data))
        data = Reservation(title=req_data['title'], email=req_data['email'],
                           availability_id=req_data['availability_id'], owner_email='ekemammezez@gmail.com')
        db.session.add(data)

        availability = Availability.query.get(req_data['availability_id'])
        availability.reserved = True

        db.session.commit()

        response_payload = {"status_code": 200, "message": "success"}
        return response_payload

    # except:
    #     response = {"status_code": 500, "message": "failed"}
    #     return response
