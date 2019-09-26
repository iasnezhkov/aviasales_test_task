from typing import Optional

from models.search import Search, search_schema, searches_schema


def diff_search_objects(first: dict, second: dict) -> dict:
    """diff to search objects
    :param first: first search object
    :param second: first search object
    :return: dict with changed fields and their values
    """
    diff_result: dict = {}

    for key, first_value in first.items():
        second_value = second.get(key)

        if isinstance(first_value, list):
            first_value = set(first_value)
            second_value = set(second_value)

            changes = first_value ^ second_value

            if changes:
                first_value = list(first_value)
                second_value = list(second_value)
            else:
                first_value = None
                second_value = None

        if first_value != second_value:
            diff_result[key] = [first_value, second_value]

    return diff_result


def diff_searches_service(first_search_id: int, second_search_id: int) -> Optional[dict]:
    """diff two search object
    :param first_search_id: first search object id
    :param second_search_id: second search object id
    :return: diff information
    """
    first_search = Search.query.filter_by(id=first_search_id).first()
    second_search = Search.query.filter_by(id=second_search_id).first()

    if not first_search or not second_search:
        return None

    first_search_dump: dict = search_schema.dump(first_search)
    second_search_dump: dict = search_schema.dump(second_search)
    diff_result: dict = diff_search_objects(first=first_search_dump, second=second_search_dump)

    return diff_result


def get_searches_service() -> list:
    """get all searches
    :return:
    """
    searches = Search.query.all()
    searches_dump: list = searches_schema.dump(searches)
    return searches_dump
