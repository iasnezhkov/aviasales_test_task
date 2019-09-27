from unittest import TestCase, mock

from services.search_service import diff_search_objects, diff_searches_service


class SearchServiceTest(TestCase):
    def test_diff_search_service(self):
        """
        Test diff search objects
        """
        first: dict = {
            'key': 1,
            'key2': 'test',
            'key_list': [1, 2, 3],
            'key_list2': [1, 2, 3, 4],
        }
        second: dict = {
            'key': 1,
            'key2': 'test2',
            'key_list': [1, 2, 3],
            'key_list2': [1, 2, 3, 4, 5],
        }
        valid_result: dict = {'key2': ['test', 'test2'], 'key_list2': [[1, 2, 3, 4], [1, 2, 3, 4, 5]]}
        data = diff_search_objects(first=first, second=second)
        self.assertEqual(valid_result, data)

    @mock.patch('services.search_service.Search')
    @mock.patch('services.search_service.diff_search_objects', return_value={'key': ['1', '2']})
    def test_diff_searches_service_searches_exists(self, diff_search_objects_mock, search_mock):
        """
        Test diff searches controller if search objects exists
        """
        data = diff_searches_service(first_search_id=1, second_search_id=2)
        valid_data = {'key': ['1', '2']}
        self.assertEqual(valid_data, data)
