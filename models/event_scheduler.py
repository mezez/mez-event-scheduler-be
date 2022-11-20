from flask_sqlalchemy import SQLAlchemy
from dataclasses import dataclass
from datetime import date


db = SQLAlchemy()


# class CalendarYear(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(255), nullable=False)
#
# class CalendarMonth(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(255), nullable=False)
#
# class CalendarDay(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(255), nullable=False)

@dataclass
class Availability(db.Model):
    id: int
    start: int
    end: int
    av_year: int
    av_month: int
    av_day: int
    av_date: date
    reserved: bool

    id = db.Column(db.Integer, primary_key=True)
    start = db.Column(db.Integer, nullable=False)
    end = db.Column(db.Integer, nullable=False)
    av_year = db.Column(db.Integer, nullable=False)
    av_month = db.Column(db.Integer, nullable=False)
    av_day = db.Column(db.Integer, nullable=False)
    av_date = db.Column(db.Date, nullable=False)
    reserved = db.Column(db.Boolean, default=False)


@dataclass
class Reservation(db.Model):
    id: int
    title: str
    owner_email: str
    email: str
    availability_id: int

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    owner_email = db.Column(db.String(255), nullable=True)
    email = db.Column(db.String(255), nullable=False)
    availability_id = db.Column(db.Integer, nullable=False)
