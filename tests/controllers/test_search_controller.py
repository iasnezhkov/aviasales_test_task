from unittest import TestCase, mock

from controllers.search_controller import diff_searches_controller


class SearchControllerTest(TestCase):
    @mock.patch('controllers.search_controller.diff_searches_service', return_value={})
    def test_diff_searches_controller_valid_query(self, diff_searches_service):
        """
        Test diff searches controller if url query is valid
        """
        url_query: dict = {
            'first_search_id': 1,
            'second_search_id': 2,
        }
        data, status_code = diff_searches_controller(url_query=url_query)
        self.assertEqual(200, status_code)

    @mock.patch('controllers.search_controller.diff_searches_service', return_value={})
    def test_diff_searches_controller_invalid_query(self, diff_searches_service):
        """
        Test diff searches controller if url query is empty
        """
        url_query: dict = {}
        data, status_code = diff_searches_controller(url_query=url_query)
        self.assertEqual(400, status_code)
        self.assertEqual({'errors': True, 'url_query': False}, data)

    @mock.patch('controllers.search_controller.diff_searches_service', return_value={})
    def test_diff_searches_controller_without_second_search_id(self, diff_searches_service):
        """
        Test diff searches controller if 'second_search_id' not given
        """
        url_query: dict = {
            'first_search_id': 1
        }
        data, status_code = diff_searches_controller(url_query=url_query)
        self.assertEqual(400, status_code)
        self.assertEqual({'errors': True, 'second_search_id': False}, data)

    @mock.patch('controllers.search_controller.diff_searches_service', return_value={})
    def test_diff_searches_controller_without_first_search_id(self, diff_searches_service):
        """
        Test diff searches controller if 'first_search_id' not given
        """
        url_query: dict = {
            'second_search_id': 2
        }
        data, status_code = diff_searches_controller(url_query=url_query)
        self.assertEqual(400, status_code)
        self.assertEqual({'errors': True, 'first_search_id': False}, data)
