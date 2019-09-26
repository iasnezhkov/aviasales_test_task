from unittest import TestCase, mock

from autoapp import application
from blueprints import API_URL_PREFIX

resource_prefix: str = 'product'
get_products_route: str = '/'


class ProductRoutesExistsTest(TestCase):
    def setUp(self) -> None:
        application.testing = True
        self.client = application.test_client()

    @mock.patch('routes.product_route.get_products_controller', return_value=({}, 200,))
    def test_get_products_route_exists(self, get_products_controller) -> None:
        """
        Test check products route are exists
        """
        endpoint: str = API_URL_PREFIX + resource_prefix + get_products_route
        response = self.client.get(endpoint)
        status_code: int = response.status_code
        self.assertNotEqual(status_code, 404)
