from unittest import TestCase, mock

from autoapp import application
from blueprints import API_URL_PREFIX

resource_prefix: str = 'search'
diff_searches_route: str = '/diff'
get_searches_route: str = '/'


class SearchRoutesExistsTest(TestCase):
    def setUp(self) -> None:
        application.testing = True
        self.client = application.test_client()

    @mock.patch('routes.search_route.diff_searches_controller', return_value=({}, 200,))
    def test_diff_searches_route_exists(self, diff_searches_controller) -> None:
        """
        Test check diff searches route are exists
        """
        endpoint: str = API_URL_PREFIX + resource_prefix + diff_searches_route
        response = self.client.get(endpoint)
        status_code: int = response.status_code
        self.assertNotEqual(status_code, 404)

    @mock.patch('routes.search_route.get_searches_controller', return_value=({}, 200,))
    def test_get_searches_route_exists(self, diff_searches_controller) -> None:
        """
        Test check get searches route are exists
        """
        endpoint: str = API_URL_PREFIX + resource_prefix + get_searches_route
        response = self.client.get(endpoint)
        status_code: int = response.status_code
        self.assertNotEqual(status_code, 404)
