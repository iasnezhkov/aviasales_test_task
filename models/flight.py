from sqlalchemy.dialects.postgresql import JSON
import datetime

from extensions import db, ma


class Flight(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    type = db.Column(db.String(10))
    carrier = db.Column(JSON)
    flight_number = db.Column(db.Integer())
    origin = db.Column(db.String(4))
    destination = db.Column(db.String(4))
    departure_date = db.Column(db.DateTime())
    arrival_date = db.Column(db.DateTime())
    flight_class = db.Column(db.String(1))
    stops = db.Column(db.Integer())
    fare_basis = db.Column(db.String(255))
    warning_text = db.Column(db.String(255))
    ticket_type = db.Column(db.String(1))
    duration = db.Column(db.Integer())
    product_id = db.Column(db.Integer(), db.ForeignKey('product.id'))

    def __repr__(self):
        return self.fare_basis


class FlightSchema(ma.Schema):
    class Meta:
        fields: tuple = (
            'id', 'type', 'carrier', 'flight_number', 'origin', 'destination', 'departure_date', 'arrival_date',
            'flight_class', 'stops', 'fate_basis', 'warning_text', 'ticket_type', 'duration',
        )


flight_schema = FlightSchema(many=True)
