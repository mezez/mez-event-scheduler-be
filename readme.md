# Event Scheduler Backend

This project is the implementation of a backend application for scheduling events on a calendar.

## Recommended IDE

Pycharm

## Project Setup
- Install dependencies
```sh
pip install -r requirements.txt
```
```sh
docker compose pull db
```
```sh
docker compose up
```

### Run Server

- If using pycharm, you can find guide to setup venv at https://www.jetbrains.com/help/pycharm/creating-virtual-environment.html#python_create_virtual_env if not automatically setup
- [optional] If you change the local mysql port in the docker-compose file, update the config.ini file to reflect your selected port as well
- Connect to your running MySQL instance using any client of your choice (eg sqlyog). According to the default docker compose file, this shouls be running on port 33066 with "root" as username and password
- Create db with name "calendar_event_scheduler". 
- For the first run uncomment # db.create_all() in line 48 of the main.py to ensure the tables for the database are created
- Run main.py to start server
- If everything is successful, comment out the db.create_all() in the main.py file to prevent recreating the tables on subsequent runs


## Implemented Features/Endpoints:

See Full documentation with sample requests and responses at https://documenter.getpostman.com/view/6071478/2s8YmULKZ3

You can click on run in postman at the top right corner to test it out.

ENDPOINTS

- [server url]/api/availabilities/create [add new availability]:
- [server url]/api/availabilities/ [list availabilities]
- [server url]/api/availabilities-by-date/<int:day>/<int:month>/<int:year> [list availabilities by date]
- [server url]/api/availabilities/delete/<int:id> [delete availability]
- 
- [server url]/api/reservations/create' [add new reservation]
- [server url]/api/reservations' [list reservations]
- [server url]/api/reservations/delete/<int:id> [delete reservation]

- **EXTRA**

  - Daily request logs can be found in the logs folder

  - The frontend for this application can be found at https://github.com/mezez/mez-event-scheduler-fe
