from django.test import TestCase
from unittest.mock import patch
from datetime import date, timedelta

from yyw_test.integrations.openweathermap.models import City
from yyw_test.integrations.openweathermap.api import search_city_by_name, get_current_temperatures_and_humidity_by_city_id

CITY_LIST = [
    {'external_id': 123, 'name': 'York', 'country': 'GB'},
    {'external_id': 124, 'name': 'New York', 'country': 'US'},
    {'external_id': 125, 'name': 'London', 'country': 'GB'},
    {'external_id': 126, 'name': 'Rome', 'country': 'IT'},
    {'external_id': 127, 'name': 'Paris', 'country': 'FR'},
    {'external_id': 128, 'name': 'Berlin', 'country': 'DE'},
    {'external_id': 129, 'name': 'Madrid', 'country': 'SP'},
]


class TestSearch(TestCase):

    def setUp(self):
        for row in CITY_LIST:
            city = City(external_id=row.external_id, name=row.name, country=row.country)
            city.save()

    def test_corrects_results_in_list(self):
        search_results = search_city_by_name('york', 5)
        is_york_in_result = any([(result['name'] == 'York') for result in search_results])
        is_new_york_in_result = any([(result['name'] == 'New York') for result in search_results])
        self.assertTrue(is_york_in_result)
        self.assertTrue(is_new_york_in_result)

    def test_wrong_results_not_in_list(self):
        search_results = search_city_by_name('york', 5)
        is_rome_in_result = any([(result['name'] == 'Rome') for result in search_results])
        self.assertFalse(is_rome_in_result)

    def test_number_of_search(self):
        total_city = City.objects.all().count()
        self.assertTrue(total_city > 5)
        search_results = search_city_by_name('york', 5)
        self.assertTrue(len(search_results) < 5)


class TestCurrentTemperature(TestCase):

    def test_stuff(self):
        example_forecast = []
        for c in range(0, 15):
            day = {
                'day': date(1, 6, 2016) + timedelta(days=c),
                'day': 20,
                'min': 20,
                'max': 22,
                'night': 22,
                'eve': 24,
                'morn': 24,
                'humidity': 99
            }
            example_forecast.append(day)
        module_name = 'yyw_test.integrations.openweathermap.api'
        with patch('{}.fetch_temperature_forecast_by_city_id'.format(module_name)) as mock_fetch:
            mock_fetch.return_value = example_forecast
            today = get_current_temperatures_and_humidity_by_city_id(123)
            self.assertEqual(today['max'], 24)
            self.assertEqual(today['min'], 20)
            self.assertEqual(today['average'], 22)
            self.assertEqual(today['humidity'], 99)
