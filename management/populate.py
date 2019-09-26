from flask.cli import AppGroup
from flask.cli import with_appcontext
from flask import current_app

from utils.parser import FileParser
from extensions import db
from models.flight import Flight
from models.product import Product
from models.search import Search

populate_cli = AppGroup('populate')


def populate() -> bool:
    """ populate database from all dumps
    :return:
    """
    file_storage: str = current_app.config.get('FILE_STORAGE')
    file_parser = FileParser(storage_path=file_storage)
    parsed_results: dict = file_parser.parse_storage()

    for filename, search in parsed_results.items():
        products: list = search.pop('products', [])
        new_search = Search(filename=filename, **search)
        db.session.add(new_search)
        db.session.commit()
        print(new_search)

        for product in products:
            flights: list = product.pop('flights', [])
            new_product = Product(search_id=new_search.id, **product)
            db.session.add(new_product)
            db.session.commit()

            for flight in flights:
                new_flight = Flight(product_id=new_product.id, **flight)
                db.session.add(new_flight)
                db.session.commit()

    return True


@populate_cli.command('populate')
@with_appcontext
def populate_command():
    populate()
