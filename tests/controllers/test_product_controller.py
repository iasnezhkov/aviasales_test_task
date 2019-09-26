from unittest import TestCase, mock

from controllers.product_controller import get_products_controller


class ProductControllerTest(TestCase):
    @mock.patch('controllers.product_controller.get_products_service', return_value=[])
    def test_get_product_controller_valid_query(self, get_product_service):
        """
        Test get products controller if url query is valid
        """
        url_query: dict = {
            'origin': 'test',
            'destination': 'test',
            'sort': '-test',
            'flight_type': 'oneway',
        }
        data, status_code = get_products_controller(url_query=url_query)
        self.assertEqual(200, status_code)

    @mock.patch('controllers.product_controller.get_products_service', return_value=[])
    def test_get_product_controller_invalid_query(self, get_product_service):
        """
        Test get products controller if url query is empty
        """
        url_query: dict = {}
        data, status_code = get_products_controller(url_query=url_query)
        self.assertEqual(400, status_code)
        self.assertEqual({'errors': True, 'url_query': False}, data)

    @mock.patch('controllers.product_controller.get_products_service', return_value=[])
    def test_get_product_controller_without_origin(self, get_product_service):
        """
        Test get products controller if 'origin' not given
        """
        url_query: dict = {
            'destination': 'test'
        }
        data, status_code = get_products_controller(url_query=url_query)
        self.assertEqual(400, status_code)
        self.assertEqual({'errors': True, 'origin': False}, data)

    @mock.patch('controllers.product_controller.get_products_service', return_value=[])
    def test_get_product_controller_without_destination(self, get_product_service):
        """
        Test get products controller if 'destination' not given
        """
        url_query: dict = {
            'origin': 'test'
        }
        data, status_code = get_products_controller(url_query=url_query)
        self.assertEqual(400, status_code)
        self.assertEqual({'errors': True, 'destination': False}, data)
