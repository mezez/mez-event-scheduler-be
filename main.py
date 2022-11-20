import configparser

from flask import Flask
from flask_restful import Api
from flask_cors import CORS
from models.event_scheduler import db


from resources.availability_create import AvailabilityCreate
from resources.reservation_create import ReservationCreate
from resources.availability_read import AvailabilityRead
from resources.reservation_read import ReservationRead

config = configparser.ConfigParser()
config.read('config.ini')
db_url = config.get('general', 'db_url')

app = Flask(__name__)
cors = CORS(app, resources={r"*": {"origins": "*"}})
app.config['SQLALCHEMY_DATABASE_URI'] = db_url

with app.app_context():
    db.init_app(app)

    # run first time and remove
    # db.create_all()

    api = Api(app)


api.add_resource(AvailabilityCreate, '/availabilities/create')
api.add_resource(AvailabilityRead, '/availabilities/')
api.add_resource(ReservationCreate, '/reservations/create')
api.add_resource(ReservationRead, '/reservations')

# api.add_resource(Delete, '/console/<string:something>/<int:somethingElse')
# api.add_resource(Delete, '/console/bin-delete')

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
