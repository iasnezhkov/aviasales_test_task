from sqlalchemy.dialects.postgresql import ARRAY

from extensions import db, ma


class Search(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    types = db.Column(db.ARRAY(db.String(10)))
    origins = db.Column(db.ARRAY(db.String(4)))
    destinations = db.Column(db.ARRAY(db.String(4)))
    departure_dates = db.Column(db.ARRAY(db.String(10)))
    return_dates = db.Column(db.ARRAY(db.String(10)))
    adults = db.Column(db.Integer())
    childs = db.Column(db.Integer())
    infants = db.Column(db.Integer())
    flight_classes = db.Column(ARRAY(db.String(1)))
    airlines = db.Column(ARRAY(db.String(2)))
    filename = db.Column(db.String(255))

    def __repr__(self):
        return self.filename


class SearchSchema(ma.Schema):
    class Meta:
        fields: tuple = (
            'id', 'type', 'origins', 'destination', 'departure_dates', 'return_dates', 'adults', 'childs', 'infants',
            'types',
        )


search_schema = SearchSchema()
searches_schema = SearchSchema(many=True)
