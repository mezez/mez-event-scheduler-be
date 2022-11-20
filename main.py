import configparser

from flask import Flask
from flask_restful import Api
from flask_cors import CORS
from models.event_scheduler import db

from resources.availability_create import AvailabilityCreate
from resources.reservation_create import ReservationCreate
from resources.availability_read import AvailabilityRead
from resources.date_availability_read import AvailabilityByDate
from resources.reservation_read import ReservationRead
from resources.reservation_delete import ReservationDelete
from resources.availability_delete import AvailabilityDelete

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


api.add_resource(AvailabilityCreate, '/api/availabilities/create')
api.add_resource(AvailabilityRead, '/api/availabilities')
api.add_resource(AvailabilityByDate, '/api/availabilities-by-date/<int:day>/<int:month>/<int:year>')
api.add_resource(ReservationCreate, '/api/reservations/create')
api.add_resource(ReservationRead, '/api/reservations')

api.add_resource(AvailabilityDelete, '/api/availabilities/delete/<int:id>')
api.add_resource(ReservationDelete, '/api/reservations/delete/<int:id>')

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
