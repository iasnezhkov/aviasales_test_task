from sqlalchemy import desc

from models.product import Product, product_schema


def get_products_service(origin: str, destination: str, flight_type: str = 'oneway', sort_by: str = '',
                         sort_desc: bool = False) -> list:
    """Get products by points with optional sorting
    :param origin: start point in IATA format
    :param destination: end point in IATA format
    :param flight_type: flight type: `oneway` or `round`
    :param sort_by: field for sorting: `total_price`, `total_duration` or `optimal`
    :param sort_desc: descending sorting
    :return: list with products
    """
    products = Product.query.filter_by(origin=origin, destination=destination, type=flight_type)

    if sort_by == 'optimal':
        sort_by = ('total_price', 'total_duration')
    elif sort_by:
        sort_by = (sort_by,)

    if sort_by and sort_desc:
        products = products.order_by(desc(*sort_by))

    if sort_by:
        products = products.order_by(*sort_by)

    products_dump: list = product_schema.dump(products)

    return products_dump
