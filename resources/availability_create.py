import json
import sys
import configparser
from xml.dom import ValidationErr

import requests
from flask_restful import Resource
from flask import request, jsonify

from helpers import my_helper
from schemas.availability_create_schema import CreateSchema
from models.event_scheduler import Availability, db


# config = configparser.ConfigParser()
# config.read('config/config.ini')
# channel_console_url = config.get('general', 'base_url')


class AvailabilityCreate(Resource):

    # @jwt_required()
    # @auth.login_required
    def post(self):
        try:
            # validation
            create_schema = CreateSchema()
            errors = create_schema.validate(request.json)
            if errors:
                return errors, 422

            req_data = request.get_json()
            # save data
            my_helper.saveLog("create-req:::" + json.dumps(req_data))
            data = Availability(start=req_data['start'], end=req_data['end'], av_year=req_data['year'],
                                av_month=req_data['month'], av_day=req_data['day'], av_date=req_data['av_date'])
            db.session.add(data)
            db.session.commit()
            response_data = {
                "message": "success",
                "info": "kflf"
            }

            response_payload = {"status_code": 200, "message": "success"}
            return response_payload

        except:
            response = {"status_code": 500, "message": "failed"}
            return response
