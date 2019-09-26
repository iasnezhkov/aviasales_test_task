from flask import request, jsonify

from blueprints import product
from controllers.product_controller import get_products_controller


@product.route('/', methods=['GET'])
def get_products_route():
    """
    Get products
    ---
    tags:
      - product
    parameters:
      - in: query
        name: origin
        required: true
        schema:
          type: string
      - in: query
        name: destination
        required: true
        schema:
          type: string
      - in: query
        name: sort
        schema:
          type: string
      - in: query
        name: flight_type
        schema:
          type: string
    responses:
      200:
        description: products data; {'errors': false, 'result': []}
      400:
        description: errors; {'errors': true, **errors}
    """
    url_query = request.args
    result, code = get_products_controller(url_query=url_query)

    return jsonify(result), code
