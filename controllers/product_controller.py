from typing import Tuple

from services.product_service import get_products_service


def get_products_controller(url_query: dict) -> Tuple[dict, int]:
    """validate get products query
    :param url_query: url query
    :return: result and status code
    """
    response: dict = {'errors': False}

    if not url_query:
        response['url_query'] = False
        response['errors'] = True

    if response.get('errors') is True:
        return response, 400

    origin = url_query.get('origin', '')

    if not origin:
        response['origin'] = False
        response['errors'] = True

    destination = url_query.get('destination', '')

    if not destination:
        response['destination'] = False
        response['errors'] = True

    if response.get('errors') is True:
        return response, 400

    sort = url_query.get('sort', '')
    sort_desc: bool = False

    if sort and sort.startswith('-'):
        sort_desc = True
        sort = sort[1:]

    if sort and sort not in ('total_price', 'total_duration', 'optimal'):
        sort = None

    flight_type = url_query.get('flight_type', 'oneway')

    if flight_type not in ('oneway', 'round'):
        flight_type = 'oneway'

    result: list = get_products_service(origin=origin, destination=destination, flight_type=flight_type, sort_by=sort,
                                        sort_desc=sort_desc)
    response['result'] = result

    return response, 200
