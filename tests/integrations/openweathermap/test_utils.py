import ujson as json
from os.path import join, dirname
from django.test import TestCase
from unittest.mock import patch
from datetime import date

from yyw_test.integrations.openweathermap.utils import fetch_temperature_and_humidity_forecast_by_city_id

BASE_DIR = dirname(__file__)
DATA_DIR = join(BASE_DIR, 'data')


def _get_data_from_file(filename):
    file_pointer = open(join(DATA_DIR, filename), 'r')
    data = json.load(file_pointer)
    return data


class TestFetchForecast(TestCase):

    def test_standard_reponse(self):
        module_name = 'yyw_test.integrations.openweathermap.utils'
        with patch('{}.requests.get'.format(module_name)) as mock_request:
            mock_request.json.return_value = _get_data_from_file('forecast_response.json')
            fetched_data = fetch_temperature_and_humidity_forecast_by_city_id(123)
            self.assertEqual(len(fetched_data), 16)
            first_day = fetched_data[0]
            self.assertEqual(first_day['date'], date(20, 11, 2016))
            self.assertEqual(first_day['day'], 5)
            self.assertEqual(first_day['min'], 5)
            self.assertEqual(first_day['max'], 5.1)
            self.assertEqual(first_day['night'], 5.1)
            self.assertEqual(first_day['eve'], 5)
            self.assertEqual(first_day['morn'], 5)
            self.assertEqual(first_day['humidity'], 98)
