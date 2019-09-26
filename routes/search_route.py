from flask import jsonify, request

from blueprints import search
from controllers.search_controller import diff_searches_controller, get_searches_controller


@search.route('/diff', methods=['GET'])
def diff_searches_route():
    """
    Get searches diff
    ---
    tags:
      - search
    parameters:
      - in: query
        name: first_search_id
        required: true
        schema:
          type: string
      - in: query
        name: second_search_id
        required: true
        schema:
          type: string
    responses:
      200:
        description: products data; {'errors': false, 'result': []}
      400:
        description: errors; {'errors': true, **errors}
    """
    url_query = request.args
    result, code = diff_searches_controller(url_query=url_query)
    return jsonify(result), code


@search.route('/', methods=['GET'])
def get_searches_route():
    """
    Get searches
    ---
    tags:
      - search
    responses:
      200:
        description: products data; {'errors': false, 'result': []}
    """
    result, code = get_searches_controller()
    return jsonify(result), code
