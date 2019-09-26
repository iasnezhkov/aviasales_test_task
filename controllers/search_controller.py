from typing import Tuple

from services.search_service import diff_searches_service, get_searches_service


def diff_searches_controller(url_query: dict) -> Tuple[dict, int]:
    """validate diff searches query
    :param url_query: url query
    :return: result and status code
    """
    response: dict = {'errors': False}

    if not url_query:
        response['url_query'] = False
        response['errors'] = True

    if response.get('errors') is True:
        return response, 400

    first_search_id = url_query.get('first_search_id')

    if not first_search_id:
        response['first_search_id'] = False
        response['errors'] = True

    second_search_id = url_query.get('second_search_id')

    if not second_search_id:
        response['second_search_id'] = False
        response['errors'] = True

    if first_search_id == second_search_id:
        response['identical_ids'] = True
        response['errors'] = True

    if isinstance(first_search_id, str) and isinstance(second_search_id, str):
        if first_search_id.isnumeric() and second_search_id.isnumeric():
            first_search_id = int(first_search_id)
            second_search_id = int(second_search_id)
        else:
            response['search_id_type'] = True
            response['errors'] = True

    if response.get('errors') is True:
        return response, 400

    result: dict = diff_searches_service(first_search_id=first_search_id, second_search_id=second_search_id)

    if isinstance(result, dict):
        response['result'] = result
        return response, 200

    response['errors'] = True
    response['message'] = 'Check search ids are exists'

    return response, 400


def get_searches_controller() -> Tuple[dict, int]:
    response: dict = {'errors': False}
    result: list = get_searches_service()
    response['result'] = result

    return response, 200
