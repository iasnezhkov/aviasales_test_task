from sqlalchemy.dialects.postgresql import ARRAY, JSON
from marshmallow import fields

from extensions import db, ma
from models.flight import flight_schema


class CastingArray(ARRAY):
    def bind_expression(self, value):
        return db.cast(value, self)


class Product(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    type = db.Column(db.String(10))
    origin = db.Column(db.String(4))
    destination = db.Column(db.String(4))
    adults = db.Column(db.Integer())
    childs = db.Column(db.Integer())
    infants = db.Column(db.Integer())
    flights = db.relationship('Flight')
    total_duration = db.Column(db.Integer())
    prices = db.Column(CastingArray(JSON))
    total_price = db.Column(db.Float())
    price_currency = db.Column(db.String(3))
    airlines = db.Column(ARRAY(db.String(2)))
    departure_date = db.Column(db.Date())
    return_date = db.Column(db.Date())
    flight_classes = db.Column(ARRAY(db.String(1)))
    search_id = db.Column(db.Integer(), db.ForeignKey('search.id'))

    def __repr__(self):
        return '{origin} - {destination}'.format(origin=self.origin, destination=self.destination)


class ProductSchema(ma.Schema):
    flights = fields.Nested(flight_schema)

    class Meta:
        fields: tuple = (
            'id', 'type', 'origin', 'destination', 'adults', 'childs', 'infants', 'flights', 'total_duration', 'prices',
            'total_price', 'price_currency', 'airlines',
        )


product_schema = ProductSchema(many=True)
