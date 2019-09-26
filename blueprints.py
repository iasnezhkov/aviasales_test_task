from flask import Blueprint

API_URL_PREFIX: str = '/api/v1/'


def _factory(partial_module_string: str, api_url_prefix: str):
    name: str = partial_module_string
    import_name: str = 'routes.{}'.format(partial_module_string)
    blueprint = Blueprint(name, import_name, url_prefix=API_URL_PREFIX + api_url_prefix)

    return blueprint


search = _factory('search_route', 'search')
product = _factory('product_route', 'product')

http_blueprints: tuple = (search, product,)
