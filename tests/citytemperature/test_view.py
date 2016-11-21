from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from unittest.mock import patch

from yyw_test.integrations.openweathermap.models import City


class CitySearchTests(APITestCase):

    def setUp(self):
        city = City(external_id=123, name='London', country='GB')
        city.save()
        self.city = city

    def test_base_usage(self):
        """since the view is not doing anything smart test that at least can be called
        witout any exception raised
        """
        url = '/api/v1.0/city/?q=london'
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class ForecastTests(APITestCase):

    def setUp(self):
        city = City(external_id=123, name='London', country='GB')
        city.save()
        self.city = city

    def test_base_usage(self):
        """since the view is not doing anything smart test that at least can be called
        witout any exception raised
        """
        url = reverse('api:forecast', kwargs={'city_id': self.city.id})
        module_name = 'yyw_test.citytemperature.views'
        with patch('{}.get_current_temperatures_and_humidity_by_city_id'.format(module_name)) as mock_api:
            mock_api.return_value = {'min': 3.77, 'max': 8.79, 'average': 6.31, 'humidity': 0}
            response = self.client.get(url, None, format='json')
            self.assertEqual(response.status_code, status.HTTP_200_OK)
